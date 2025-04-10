# pdfsp/cli.py

from pdfsp import extract_tables_from_pdf
from pdfsp import extract_tables

import sys

def console_extract_tables():

    if len(sys.argv) > 2:
        source_folder = sys.argv[1]
        output_folder = sys.argv[2]
    elif len(sys.argv) > 1:
        source_folder = sys.argv[1]
        output_folder = None
    elif len(sys.argv) == 1:
        source_folder = "."
        output_folder = None

    extract_tables(source_folder, output_folder)

