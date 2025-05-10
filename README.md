# 📄 pdfsp
---

**`pdfsp`** is a Python package that extracts tables from PDF files and saves them to Excel. It also provides a simple Streamlit app for interactive viewing of the extracted data.

---

## 🚀 Features

- Extracts tabular data from PDFs using `pdfplumber`
- Converts tables into `pandas` DataFrames
- Saves output as `.xlsx` Excel files using `openpyxl`
- Ensures column names are unique to prevent issues
- Visualizes DataFrames with `streamlit`

---

## 📦 Installation

Make sure you're using **Python 3.10 or newer**, then install with:

```bash
pip install pdfsp -U

```



### python script 
```python
# pdf.py 
from pdfsp import extract_tables

source_folder = "."
output_folder = "output"

extract_tables(source_folder, output_folder )

```

### From console / Terminal / Command Line 

```bash 
# all tables from all pdf files in the current folder to current folder 
pdfsp . . 
# all tables from all pdf files in someFolder to current SomeOutFolder 
pdfsp someFolder SomeOutFolder 


# all tables of some.pdf to the current folder 
pdfsp some.pdf .

# all tables of some.pdf to the toThisFolder folder 
pdfsp some.pdf toThisFolder

```


