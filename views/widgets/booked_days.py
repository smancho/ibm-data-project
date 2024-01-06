from data import csv
import altair as alt
import pandas as pd
import streamlit as st


def render():
    data = csv.get_booked_days_by("neighbourhood_group")
    source = {
        "neighbourhood_group": [],
        "days_booked_365": [],
    }
    # add to the source the neighbourhood group and the days booked
    for neighborhood_group, days_booked_365 in data.items():
        source["neighbourhood_group"].append(neighborhood_group)
        source["days_booked_365"].append(days_booked_365)

    base = alt.Chart(pd.DataFrame(source)).encode(
        alt.Theta("days_booked_365:Q", stack=True, title="Days booked"),
        alt.Radius("days_booked_365").scale(type="sqrt", zero=True, rangeMin=20),
        alt.Color("neighbourhood_group:N", title="Neighborhood group"),
    )
    c1 = base.mark_arc(innerRadius=20, stroke="#fff")
    c2 = base.mark_text(radiusOffset=10).encode(
        text=alt.Text("days_booked_365:N").format(".0f")
    )
    st.write("### Days booked by neighbourhood group")
    st.altair_chart(
        (c1 + c2).interactive(),
        use_container_width=True,
    )
