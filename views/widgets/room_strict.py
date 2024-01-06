from data import csv
import streamlit as st
import pandas as pd
import numpy as np


def render():
    room_types = csv.get_room_with_cancellation_policy("strict")
    st.write("## Rooms with strict cancellation policy")
    st.table(room_types)
