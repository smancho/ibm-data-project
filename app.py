"""Streamlit application"""

import streamlit as st
import streamlit_option_menu
from views import data, about, dashboard


def sidebar():
    with st.sidebar:
        streamlit_option_menu.option_menu(
            "Main Menu",
            ["Dashboard", "Data", "About"],
            icons=["bar-chart", "database", "info-circle"],
            menu_icon="cast",
            default_index=0,
            key="page",
        )


def main():
    sidebar()
    page = st.session_state.get("page", "Dashboard")

    if page == "Dashboard" or page is None:
        dashboard.render()
    elif page == "Data":
        data.render()
    elif page == "About":
        about.render()


if __name__ == "__main__":
    st.set_page_config(page_title="IBM: Airbnb dashboard", layout="wide")
    st.title("IBM: Airbnb dashboard")
    main()
