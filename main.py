
from pdfsp import extract_tables , extract_tables_from_pdf
import pandas as pd 
folder = "." #  r"C:\Users\Username\SomeFolder"
# extract_tables(folder, "out3")
dfs = extract_tables_from_pdf("aa.pdf")
print(dfs[0].df )
df = dfs[0].df 
# Make column names unique
# df.columns = pd.io.parsers.ParserBase({'names': df.columns})._maybe_dedup_names(df.columns)
# df = df.loc[:, ~df.columns.duplicated()]
def make_unique(cols) :
    a = [] 
    b = [] 
    for i ,  col in enumerate( cols)  : 
        ucol = col 
        if col in a : 
            col = col + str(i)
            ucol =  f"{col}-{i}"
        a.append(col )
        b.append(ucol )
    return b 
def make_unique_cols(df):
    cols = [str(x) for x in df.columns ]
    df.columns = make_unique(cols)
    return df 
import streamlit as st
import pandas as pd
df = make_unique_cols(df )
# Streamlit app
st.title("Simple Webpage from DataFrame")
st.write(df)