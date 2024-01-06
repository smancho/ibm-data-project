import altair as alt
import streamlit as st
import pandas as pd
from data import csv


def get_price_rounded(price):
    try:
        return round(float(price), 2)
    except ValueError:
        return "N/A"


def render(field="neighbourhood_group"):
    room_prices = csv.get_prices_grouped_by(field)
    chart = (
        alt.Chart(room_prices.reset_index())
        .mark_bar()
        .encode(
            x=alt.X("total_price:Q", title="Price"),
            y=alt.Y(
                f"{field}:N",
                sort=alt.EncodingSortField(
                    field="total_price", op="sum", order="descending"
                ),
                title=field.replace("_", " ").title(),
            ),
            tooltip=[
                alt.Tooltip("total_price:Q", title="Price"),
                alt.Tooltip(f"{field}:N", title=field.replace("_", " ").title()),
            ],
        )
        .properties(width=800, height=400)
        .configure_axis(labelFontSize=15, titleFontSize=15)
    )

    st.altair_chart(chart, use_container_width=True)
    st.write(
        f"💵 **{room_prices.index[0]}** is the most expensive with and average price of",
        get_price_rounded(room_prices.values[0]),
        "$",
    )
    # get the cheapest room excluding the values that are not numbers
    room_prices = room_prices[room_prices.values != "nan"]
    st.write(
        f"💵 **{room_prices.index[-1]}** is the cheapest with and average price of",
        get_price_rounded(room_prices.values[-1]),
        "$",
    )
