# lib used
import os

import pandas as pd


def get_data():
    """
    read data and return pandas dataframe
    """

    pwd = os.getcwd()
    listing_data = os.path.join(pwd, "data/raw/bkk_listings.csv")
    df = pd.read_csv(listing_data)
    return df


def get_avg_neighbourhood_price(df):
    """
    Core solution, suggesting price recommendation based on average price of the neighbourhood
    """

    df_filt = df.drop(df[df["price"].isna()].index)
    avg_price = (
        df_filt.groupby(by="neighbourhood", as_index=False)["price"].mean().round(2)
    )
    return avg_price


def write_data():
    """
    write cooked data ready for consumption
    """

    get_avg_neighbourhood_price(get_data()).to_csv(
        os.path.join(os.getcwd(), "data/cal/avg_price.csv")
    )


if __name__ == "__main__":
    write_data()
