import streamlit as st
from data import csv


def render():
    st.title("CSV Raw data")
    df = csv.read_as_dataframe()
    st.dataframe(df)
    # write the numner of rows
    st.write("Number of rows: ", df.shape[0])
