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
from pdfsp import extract_tables, Options
from pdfsp.cli import console_extract_tables_helper
import pytest
SAMPLE_URL = "https://sample-files.com/downloads/documents/pdf/sample-report.pdf"
OUTPUT_FOLDER = "ignore_output"

def test_full(capsys):

    with capsys.disabled():
        source_folder = "."
        output_folder = OUTPUT_FOLDER
        options = Options(source_folder=source_folder, output_folder=output_folder)

        extract_tables(options)


def test_full_combine(capsys):

    with capsys.disabled():
        source_folder = None
        output_folder = None  
        options = Options(
            source_folder=source_folder, output_folder=output_folder, combine=True
        )

        extract_tables(options)

def test_full_skiprows(capsys):

    from pdfsp import extract_tables , Options 
    with capsys.disabled():
        
        output_folder = OUTPUT_FOLDER 
        combine = False 
        skiprows = 0 
        options = Options(source_folder=SAMPLE_URL, output_folder=output_folder , combine=combine , skiprows=skiprows)
        extract_tables(options)

def test_cli():
    console_extract_tables_helper(
        [
            "--combine",
            "--skiprows=0",
            SAMPLE_URL , 
            OUTPUT_FOLDER ,
        ]
    )

def test_cli2():
    console_extract_tables_helper(
        [

            SAMPLE_URL , 
           OUTPUT_FOLDER ,
        ]
    )