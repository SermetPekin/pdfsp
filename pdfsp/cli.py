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
# pdfsp/cli.py


from pdfsp.core import extract_tables
import sys
from ._typing import T_OptionalPath


def console_router(
    source_folder: T_OptionalPath = None, 
    output_folder: T_OptionalPath = None
):
    """Console router"""

    if str(source_folder).endswith(".pdf"):
        source_folder = [source_folder]
    return extract_tables(source_folder, output_folder)


def console_extract_tables():
    """Console entry point"""

    if len(sys.argv) > 2:
        source_folder = sys.argv[1]
        output_folder = sys.argv[2]
    elif len(sys.argv) > 1:
        source_folder = sys.argv[1]
        output_folder = None
    elif len(sys.argv) == 1:
        source_folder = "."
        output_folder = None
    console_router(source_folder, output_folder)
