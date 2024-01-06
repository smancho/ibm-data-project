from data import csv
import altair as alt
import pandas as pd
import streamlit as st


def render():
    st.write("## Reviews effect in price")
    st.write("#### Scenario preparation")
    st.write("* Data has been groued by number of reviews using steps of 50.")
    st.write("* This has been done to reduce the number of data points.")
    st.write("* The number of reviews has been capped at 1200.")

    data_reviews = csv.get_price_for_reviews()
    chart_reviews = (
        alt.Chart(data_reviews)
        .mark_boxplot()
        .encode(
            x=alt.X(
                "number_of_reviews:Q",
                title="Reviews",
                axis=alt.Axis(tickCount=20, tickMinStep=1000),
                scale=alt.Scale(domain=(0, 1200)),
            ),
            y=alt.Y("price:Q", title="Price"),
        )
    )
    st.altair_chart(chart_reviews, use_container_width=True)

    st.write("### Inferences for reviews")
    st.write(
        """
        * In general, the number of reviews does not have a significant impact on the price.
        * But, there is a deviation in the price for the rentals with review count between 500 and 750.
        * The amount of rental with review count higher than 750 is very low.
        """
    )

    st.divider()

    st.write("## Host verification effect in price")
    data_host = csv.get_price_for_verified_host()
    chart_host = (
        alt.Chart(data_host)
        .mark_boxplot()
        .encode(
            y=alt.Y("price", title="Price"),
            x=alt.X("host_identity_verified", title="Verified host"),
        )
    )
    st.altair_chart(chart_host, use_container_width=True)
    st.write("### Inferences for host identity")
    st.write(
        """
        * The verified host identity does not have a significant impact on the price.
        * The median price for verified host identity is slightly lower than the median price for
        unverified host identity.
        """
    )
