import pdfplumber
import pandas as pd
from dataclasses import dataclass
import traceback
import os

from pathlib import Path


@dataclass
class DataFrame:
    df: pd.DataFrame
    extra: tuple
    out: str = None

    def __post_init__(self):
        if self.out is None:
            self.out = "Output"
        self.out = Path(self.out)
        self.df = self.make_unique_cols(self.df)

    def make_unique_cols(self, df):
        cols = [str(x) for x in df.columns]
        df.columns = self.make_unique(cols)
        return df

    def make_unique(self, cols):
        a = []
        b = []
        for i, col in enumerate(cols):
            ucol = col
            if col in a:

                col = col + str(i)
                ucol = f"{col}-{i}"

            a.append(col)
            b.append(ucol)

        return b

    def write(self, *args):

        os.makedirs(self.out, exist_ok=True)

        name = self.extra[0]
        string = ""
        if args:
            args = [str(x) for x in args]
            string = "-".join(args)
        file_name = f"{name}-{string}.xlsx"
        try:
            self.df.to_excel(self.out / file_name)
            print(f"[writing table] {file_name}")
        except:

            traceback.print_exc()


def get_pdf_files(folder: Path = None, out: str = None):
    if folder is None:
        folder = Path(".")
    if out is None:
        out = Path(".")

    files = [x for x in os.listdir() if x.endswith(".pdf")]
    return files


def extract_tables_from_pdf(pdf_path, out: Path = None) -> list[DataFrame]:

    pdfs = []
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        print(f"""Extracting tables from {pdf_path}""")

        name = str(pdf_path).split(".")[0]

        for page_number, page in enumerate(pdf.pages, start=1):
            # Extract tables on the current page
            tables = page.extract_tables()

            for idx, table in enumerate(tables):
                # Convert table (list of lists) to a Pandas DataFrame
                df = pd.DataFrame(
                    table[1:], columns=table[0]
                )  # Use the first row as header

                pdfs.append(DataFrame(df, (name,), out))
    return pdfs


def write_dfs(pdf_paths, out=None):

    for pdf_path in pdf_paths:
        a = extract_tables_from_pdf(pdf_path, out)
        for i, df in enumerate(a):
            df.write(i + 1)


def extract_tables(folder: Path = None, out: str = None):

    files = get_pdf_files(folder, out)

    write_dfs(files, out)


# ........................................ main
# ........................................
# pdf_paths = ["aa.pdf", "bb.pdf"]
# write_dfs(pdf_paths)
# ........................................
# write_tables_folder(".", "a3")