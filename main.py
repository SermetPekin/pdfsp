# pdf.py
from pdfsp import extract_tables, Options

# Define extraction options
source_folder = "."
output_folder = "output"
combine_tables = True

options = Options(
    source_folder=source_folder,
    output_folder=output_folder,
    combine=combine_tables
)

# Run the table extraction
extract_tables(options)




