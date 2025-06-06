pdfsp
=====

**pdfsp** is a Python package that extracts tables from PDF files and saves them to Excel. It also provides a simple Streamlit app for interactive viewing of the extracted data.

Features
--------

- Extracts tabular data from PDFs using ``pdfplumber``
- Converts tables into ``pandas`` DataFrames
- Saves output as ``.xlsx`` Excel files using ``openpyxl``
- Ensures column names are unique to prevent issues
- Visualizes DataFrames with ``streamlit``

Installation
------------

Make sure you're using **Python 3.10 or newer**, then install with:

.. code-block:: bash

    pip install pdfsp -U

Usage
-----

Python script
^^^^^^^^^^^^^

.. code-block:: python

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

Command line usage
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # Extract all tables from all PDF files in the current folder and save them to the current folder
    pdfsp . .

    # Extract and COMBINE big tables (spanning multiple pages) into single files, saved to the current folder
    pdfsp . . --combine

    # Extract all tables from PDF files in 'someFolder' and save them to 'SomeOutFolder'
    pdfsp someFolder SomeOutFolder

    # Extract all tables from 'some.pdf' and save them to the current folder
    pdfsp some.pdf .

    # Extract all tables from 'some.pdf' and save them to 'toThisFolder'
    pdfsp some.pdf toThisFolder