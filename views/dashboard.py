import streamlit as st
from views.widgets import (
    booked_days,
    construction_year,
    reviews_host_effect,
    room_price_neighborhood,
    room_price_type,
    room_strict,
    room_types,
    service_fee_price_impact,
    short_term_rentals,
)


def render():
    widget_room_types, widget_room_strict = st.columns(spec=[0.7, 0.3])
    with widget_room_types:
        # 5a-1: Enumerate the different room types
        room_types.render()

    with widget_room_strict:
        # 5a-2: Enumerate the different room types with strict cancellation policy
        room_strict.render()

    st.write("## Prices")
    (
        widget_room_fees_by_neighborhood_group,
        widget_room_fees_by_neighborhood,
    ) = st.columns(spec=[0.5, 0.5])
    with widget_room_fees_by_neighborhood_group:
        # 5a-3: Enumerate the prices by neighborhood group and also mention which is the most
        # expensive neighborhood group for the rentals.
        st.write("### By neighborhood group")
        room_price_neighborhood.render("neighbourhood_group")
    with widget_room_fees_by_neighborhood:
        # 5a-4: Enumerate the 10 most expensive neighborhoods in ascending order of price with the
        # help of a horizontal bar chart. Which is the cheapest neighborhood?
        st.write("### By neighborhood")
        room_price_neighborhood.render("neighbourhood")

    # 5a-5: Enumerate the neighborhoods that offer short term rentals of less than 10 days.
    # Illustrate with a bar chart.
    short_term_rentals.render()
    # 5a-6: Enumerate the prices with respect to the room type using a bar chart and also expose
    # your inferences.
    room_price_type.render()
    # 5a-7: Create a pie chart that shows the distribution of the days booked for each neighborhood
    # group.
    booked_days.render()

    # 5b-1: Does the service fee and the room price have a mutual impact? Illustrate this
    # relationship with a scatter plot and indicate your inferences
    service_fee_price_impact.render()
    # 5b-2: Using a line chart show in which year the maximum room construction took place.
    construction_year.render()

    # 5c: Using a box plot illustrate the effect of the number of reviews on the price:
    #   * Effect of the number of reviews on the price
    #   * Effect of the verified host identity on the price
    reviews_host_effect.render()
