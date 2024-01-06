import streamlit as st
import altair as alt
import pandas as pd
from data import csv
from typing import List


def render():
    st.write("## Service fee vs room price")

    data = csv.get_price_and_service_fee()
    chart = (
        alt.Chart(data)
        .mark_point()
        .encode(
            y=alt.Y("service_fee", title="Service fee"),
            x=alt.X("price", title="Price"),
            size=alt.Size("total_price", title="Total price"),
        )
    )
    st.altair_chart(chart, use_container_width=True)
    st.write("### Inferences")
    st.write(
        """
        * The service fee and the room price have a mutual impact.
        * The room price and the service fee are directly proportional.
        * The total price is the sum of the room price and the service fee.
        * The service is about 20% of the room price.
        """
    )
    st.write(
        """
        <code>
                price  service_fee  total_price  service_fee_percentage
        43887    50.0         10.0         60.0                    20.0
        9885     50.0         10.0         60.0                    20.0
        48916    50.0         10.0         60.0                    20.0
        40520    50.0         10.0         60.0                    20.0
        68968    50.0         10.0         60.0                    20.0
        ...       ...          ...          ...                     ...
        96835  1200.0        240.0       1440.0                    20.0
        50606  1200.0        240.0       1440.0                    20.0
        58531  1200.0        240.0       1440.0                    20.0
        76937  1200.0        240.0       1440.0                    20.0
        67377  1200.0        240.0       1440.0                    20.0
        </code>
        """,
        unsafe_allow_html=True,
    )
