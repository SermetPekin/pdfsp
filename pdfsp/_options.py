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
from ._globals import SAMPLE_PDF_file_name
from ._utils import is_url
from ._utils import check_folder

# ................................................................


@dataclass
class SourceFolder(object):
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


class PdfFile(object):
    """PDF file object."""

    def __init__(self, file: Path):
        self.file = Path(file)

    def __str__(self) -> str:
        return str(self.file)

    def __repr__(self) -> str:
        return f"PdfFile({self.file})"

    def __iter__(self):
        """Iterate over all files in the folder."""
        for file in [self.file]:
            yield file

    def __len__(self) -> int:
        return 1


class PdfFileUrl(object):
    def __init__(self, url: str = None):
        self.file = PdfFile(SAMPLE_PDF_file_name)
        self.url = url
        self._download()

    def __iter__(self):
        """Iterate over all files in the folder."""
        for file in [self.file.file]:
            yield file

    def __len__(self) -> int:
        return 1

    def _download(self):
        print(f"Downloading {self.url} to {self.file.file }")

        import requests

        response = requests.get(self.url, proxies=None)
        if response.status_code == 200:
            with open(self.file.file, "wb") as f:
                f.write(response.content)
            print(f"{self.file.file} downloaded successfully!")
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
