# This file is part of the pdfsp project
# Copyright (C) 2025 Sermet Pekin
#
# This source code is free software; you can redistribute it and/or
# modify it under the terms of the European Union Public License
# (EUPL), Version 1.2, as published by the European Commission.
#
# You should have received a copy of the EUPL version 1.2 along with this
# program. If not, you can obtain it at:
# <https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12>.
#
# This source code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# European Union Public License for more details.
#
# Alternatively, if agreed upon, you may use this code under any later
# version of the EUPL published by the European Commission.
# from dataclasses import dataclass
from dataclasses import dataclass

# ................................................................
from ._typing import T_OptionalPath, Path
from ._utils import is_url
from ._utils import check_folder

# ................................................................

from abc import ABC  , abstractmethod 


class SourceIterable(ABC):
    @abstractmethod
    def __iter__(self):
        """Iterate over all files in the folder."""
        ...

    def __len__(self) -> int:
        """Get the number of PDF files in the folder."""
        ...

@dataclass
class SourceFolder(SourceIterable):
    """Source folder for PDF files."""

    def __init__(self, folder: T_OptionalPath = None):
        if folder is None:
            folder = "."
        self.folder = Path(folder)
        if not check_folder(self.folder):
            raise ValueError(f"Invalid folder: {folder}")

    def __str__(self) -> str:
        return str(self.folder)

    def __repr__(self) -> str:
        return f"Folder({self.folder})"

    def __iter__(self):
        """Iterate over all files in the folder."""

        for file in self.folder.iterdir():
            if file.is_file() and file.suffix.lower() == ".pdf":
                yield file

    def __len__(self) -> int:
        """Get the number of PDF files in the folder."""

        return len(list(self.folder.glob("*.pdf")) + list(self.folder.glob("*.PDF")))


class PdfFile(SourceIterable):
    """PDF file object."""

    def __init__(self, file_name: Path):
        self.file_name = Path(file_name)


    def __repr__(self) -> str:
        return f"PdfFile({self.file_name})"

    def __iter__(self):
        """Iterate over all files in the folder."""
        yield from  [self.file_name]

    def __str__(self) -> str:
        return str(self.file_name)




class PdfFileUrl(PdfFile):
    def __init__(self, url: str = None ,    test = False  ):
        self.url = url
        self.file_name = self.get_file_name() 

        if test :
            return 
        self._download()
    def __repr__(self) -> str:
        return f"PdfFileUrl({self.url})"

    def __str__(self) -> str:
        return str(self.url)
    
    def get_file_name(self):
        from urllib.parse import urlparse 
        return urlparse(self.url).path.split('/')[-1]
    
    def _download(self):
        
        print(f"Downloading {self.url} to { self.file_name }")
        import requests
        response = requests.get(self.url, proxies=None)
        if response.status_code == 200:
            with open(self.file_name, "wb") as f:
                f.write(response.content)
            print(f"{self.file_name} downloaded successfully!")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")


@dataclass
class Options:
    """Options"""

    source_folder: T_OptionalPath = None
    output_folder: T_OptionalPath = None
    combine: bool = False
    skiprows: int = 0
    from_url: bool = False
    source_folder_raw: str = None
    _type: str = "folder"  # url or folder or pdf

    def __post_init__(self):

        if self.source_folder is None:
            self.source_folder = "."

        if self.output_folder is None:
            self.output_folder = "Output"

        self.source_folder_raw = self.source_folder

        self.source_folder = Path(self.source_folder)
        self.output_folder = Path(self.output_folder)
        # self.source_folder = self.source_folder.resolve()
        # self.output_folder = self.output_folder.resolve()
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.combine = True if self.combine else False

        self.source_folder = (
            [self.source_folder]
            if isinstance(self.source_folder, str)
            else self.source_folder
        )
        self.output_folder = (
            [self.output_folder]
            if isinstance(self.output_folder, str)
            else self.output_folder
        )

        if str(self.source_folder_raw).startswith("http"):
            self._type = "url"
        elif str(self.source_folder_raw).endswith(".pdf"):
            self._type = "pdf"

        if self._type == "folder":
            self.source_folder = SourceFolder(self.source_folder)

        if self._type == "pdf":
            self.source_folder = PdfFile(self.source_folder)

        if self._type == "url":
            self.source_folder = PdfFileUrl(self.source_folder_raw)

        # print(self)
