from data import csv
import altair as alt
import pandas as pd
import streamlit as st


def render():
    room_types = csv.get_room_types()
    data_total_price = csv.get_prices_grouped_by(
        group_field="room_type", price_field="total_price"
    )
    data_price = csv.get_prices_grouped_by(group_field="room_type", price_field="price")
    data_service_fee = csv.get_prices_grouped_by(
        group_field="room_type", price_field="service_fee"
    )

    # for each room type create a record that includes the room type, the total price, the price and the service fee
    data = []

    for room_type, price in data_price.items():
        data.append(
            {
                "room_type": room_type,
                "value": price,
                "type": "price",
            }
        )
    for room_type, service_fee in data_service_fee.items():
        data.append(
            {
                "room_type": room_type,
                "value": service_fee,
                "type": "service_fee",
            }
        )

    st.write("## Mean prices by room type")
    chart = (
        alt.Chart(pd.DataFrame(data))
        .mark_bar()
        .encode(
            x=alt.X("room_type", sort="-y", title="Room type"),
            y=alt.Y("value", title="Total price"),
            color="type",
            tooltip=["room_type", "type", "value"],
        )
    )
    st.altair_chart(chart, use_container_width=True)
