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
from urllib.parse import urlparse

# ................................................................
from ._typing import Path, T_Path
from ._globals import SAMPLE_PDF_file_name
from ._typing import (
    T_Path,
    T_OptionalPath,
    Generator,
    Path,
    Dict,
)


# ................................................................
def print_summary_report(report: Dict[str, Dict[str, int]]) -> None:
    """Print a summary report including how many tables were extracted per file."""
    print("\n=== 📊 Extraction Summary Report ===")

    success_files = report["success"]
    failed_files = report["failed"]

    print(f"✅ Successful Files: {len(success_files)}")
    for file, count in success_files.items():
        print(f"   - {file} → 🗂️ {count} tables extracted")

    print(f"\n❌ Failed Files: {len(failed_files)}")
    for f in failed_files:
        print(f"   - {f}")

    if not failed_files:
        print("\n🎉 All files processed successfully!")
    else:
        print("\n⚠️ Some files failed to process. See details above.")


def get_pdf_from_url(url, proxies=None):
    # raise NotImplementedError("This function is not implemented yet.")
    import requests

    file_name = SAMPLE_PDF_file_name
    response = requests.get(url, proxies=proxies)

    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"{file_name} downloaded successfully!")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


def is_url(path_or_url):
    if isinstance(path_or_url, list):
        path_or_url = path_or_url[0]
    parsed = urlparse(str(path_or_url))
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def check_folder(folder: T_Path) -> bool:
    """Check if the folder exists and is a directory."""
    folder = Path(folder)
    if not folder.exists():
        print(f"Folder `{folder}` does not exist.")
        return False
    if not folder.is_dir():
        print(f"`{folder}` is not a directory.")
        return False
    return True
