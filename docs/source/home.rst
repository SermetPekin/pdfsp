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

    pip install pdfsp

Usage
-----

Python script
^^^^^^^^^^^^^

.. code-block:: python

    # pdf.py 
    from pdfsp import extract_tables

    source_folder = "."
    output_folder = "output"

    extract_tables(source_folder, output_folder)

Command line usage
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # All tables from all PDF files in the current folder to current folder 
    pdfsp . .

    # All tables from all PDF files in someFolder to current SomeOutFolder 
    pdfsp someFolder SomeOutFolder 

    # All tables of some.pdf to the current folder 
    pdfsp some.pdf .

    # All tables of some.pdf to the toThisFolder folder 
     pdfsp some.pdf toThisFolder
