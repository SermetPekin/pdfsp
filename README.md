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

Make sure you're using **Python 3.13 or newer**, then install with:

```bash
pip install git+https://github.com/SermetPekin/pdfsp.git
```