import streamlit as sl
import pandas as pd

sl.set_page_config(layout="wide")
col1, col2 = sl.columns(2)


def make_project_columns(start, end):
    for index, row in df[start:end].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        file_path = "images/"+row["image"]
        sl.image(file_path, width=500)
        sl.write(f"[Source code]({row['url']})")


with col1:
    sl.image("images/photo.png", width=500)

with col2:
    sl.title("Zdenek")
    content = """
    biadsadifughadfiguhadfiguhadfgiudhgiuadfhgfa
    ahgahgafdighadfighadfgihadfgihadfgihafgdafighdfaghadfg
    adifhgdafhgadfghadfiughfaiu
    """
    sl.info(content)

sl.write(content)

df = pd.read_csv("data.csv", sep=";")
col3, empy_col, col4 = sl.columns([1.5, 0.5, 1.5])

with col3:
    make_project_columns(0,10)

with col4:
    make_project_columns(10,20)

