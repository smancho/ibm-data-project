from data import csv
import altair as alt
import pandas as pd
import streamlit as st


def render():
    st.write("## Construction year")

    data = csv.get_construction_year()
    line_chart = (
        alt.Chart(data)
        .mark_line()
        .encode(
            x=alt.X("construction_year", title="Year", axis=alt.Axis(format="d")),
            y=alt.Y("price", title="Rooms", scale=alt.Scale(domain=[4800, 5200])),
        )
    )
    st.altair_chart(line_chart, use_container_width=True)
