import streamlit as st
import altair as alt
import pandas as pd
from data import csv
from typing import List


def render():
    neighborhoods_max = csv.get_neighborhoods_with_min_nights_or_lower(nights=10)
    st.write("## Short therm rentals")

    bar_chart = (
        alt.Chart(neighborhoods_max)
        .mark_bar()
        .encode(
            x=alt.X("neighbourhood:O", title="Neighborhood", sort="-y"),
            y=alt.Y("minimum_nights:Q", title="Minimum nights"),
        )
    )

    st.altair_chart(bar_chart, use_container_width=True)
