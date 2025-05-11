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
from ._typing import T_OptionalPath,Path 
from ._options import Options  






def console_extract_tables():
    """Entry point for command-line interface."""
    args = sys.argv[1:]   
    combine = False

    if "--combine" in args:
        combine = True
        args.remove("--combine") 

    if len(args) >= 2:
        source = args[0]
        output = args[1]
    elif len(args) == 1:
        source = args[0]
        output = None
    else:
        source = "."
        output = None

    options = Options(source_folder=source, output_folder=output, combine=combine)
    extract_tables(options)
