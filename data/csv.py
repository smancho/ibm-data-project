import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=True, ttl=300)
def read_as_dataframe():
    """Reads the csv file"""
    df = pd.read_csv("./Airbnb_Open_Data.csv", low_memory=False)
    df.drop(["host id", "id", "country", "country code"], axis=1, inplace=True)
    df.drop_duplicates(inplace=True)
    df.rename(columns={"availability 365": "days_booked_365"}, inplace=True)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df["service_fee"] = (
        df["service_fee"].str.replace("$", "").str.replace(",", "").astype(float)
    )
    df["price"] = df["price"].str.replace("$", "").str.replace(",", "").astype(float)
    df["total_price"] = df["price"] + df["service_fee"]
    df["service_fee_percentage"] = (df["service_fee"] / df["price"]) * 100

    df["neighbourhood"] = df["neighbourhood"].apply(
        lambda x: str(x) if isinstance(x, str) else None
    )
    df["neighbourhood"] = df["neighbourhood"].str.title().astype(str)

    df["neighbourhood_group"] = df["neighbourhood_group"].str.title()
    df["neighbourhood_group"] = df["neighbourhood_group"].str.replace(
        "Manhatan", "Manhattan"
    )
    return df


def get_room_types():
    """Returns the room types"""
    df = read_as_dataframe()
    # get the room types and their counts
    room_types = df.room_type.value_counts()
    # convert the room types to a dataframe
    room_types = pd.DataFrame(room_types).reset_index()
    # rename the columns
    room_types.columns = ["room_type", "count"]
    return room_types.to_dict(orient="records")


def get_room_with_cancellation_policy(policy_name="strict"):
    """Returns the room with the cancellation policy"""
    df = read_as_dataframe()
    room_types_value_counts = df[df["cancellation_policy"] == "strict"][
        "room_type"
    ].value_counts()
    return room_types_value_counts.to_dict()


def get_prices_grouped_by(
    group_field="neighbourhood",
    price_field="total_price",
    ascending=False,
    top=10,
):
    """Returns the fees grouped by neighborhood"""
    df = read_as_dataframe()
    return (
        df.groupby(group_field)[price_field]
        .mean()
        .sort_values(ascending=ascending)
        .head(top)
    )


def get_neighborhoods_with_min_nights_or_lower(nights=10, max_or_mean="max"):
    """Returns the neighborhoods with min nights or lower"""
    df = read_as_dataframe()
    df = df[df["minimum_nights"] >= 0]
    df = df[df["minimum_nights"] <= nights]
    grouped_data = df.groupby(["neighbourhood"])
    if max_or_mean == "mean":
        grouped_data = grouped_data["minimum_nights"].mean().reset_index()
    else:
        grouped_data = grouped_data["minimum_nights"].max().reset_index()
    return grouped_data


def get_booked_days_by(field="neighbourhood_group", ascending=False):
    """Returns the booked days by neighborhood group"""
    df = read_as_dataframe()
    return df.groupby(field)["days_booked_365"].mean().sort_values(ascending=ascending)


def get_price_and_service_fee():
    """Returns the price and service fee"""
    df = read_as_dataframe()
    return (
        df[["price", "service_fee", "total_price", "service_fee_percentage"]]
        .dropna()
        .sort_values(by="price")
    )


def get_construction_year():
    """Return the sum of rooms built per year"""
    df = read_as_dataframe()
    df = df[df["construction_year"] > 0]
    df = df[df["construction_year"] < 2025]
    return df.groupby(["construction_year"])["price"].count().reset_index()


def get_price_for_verified_host():
    """Returns the price for verified host"""
    df = read_as_dataframe()
    return df[["price", "host_identity_verified"]].sort_values(by="price")


def get_price_for_reviews():
    """Returns the price for reviews"""
    df = read_as_dataframe()
    df["number_of_reviews"] = df["number_of_reviews"].apply(
        lambda x: x if x is not None else 0
    )
    # group the data in groups of 100 reviews
    df["number_of_reviews"] = df["number_of_reviews"].apply(lambda x: x // 50)
    df["number_of_reviews"] = df["number_of_reviews"].apply(lambda x: x * 50)

    return df[["price", "number_of_reviews"]].sort_values(by="number_of_reviews")
