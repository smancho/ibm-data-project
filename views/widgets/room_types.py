import streamlit as st
import altair as alt
import pandas as pd
from data import csv
from typing import List


def render():
    rooms = csv.get_room_types()
    # sort the rooms by count
    rooms = sorted(rooms, key=lambda x: x["count"], reverse=True)
    st.write("## Room Types")
    col_data, col_graph = st.columns([0.3, 0.7])
    col_data.dataframe(
        rooms, hide_index=True, column_config={"count": {"min_width": 50}}
    )

    # display the room type as a pie chart
    source = pd.DataFrame(rooms)
    chart = (
        alt.Chart(source)
        .mark_arc(innerRadius=50)
        .encode(
            theta="count:Q",
            color="room_type:N",
        )
    )
    col_graph.altair_chart(chart, use_container_width=True)
