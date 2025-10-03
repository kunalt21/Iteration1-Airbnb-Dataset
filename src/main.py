# lib used
import os

import pandas as pd


def get_data():
    pwd = os.getcwd()
    listing_data = os.path.join(pwd, "data/raw/bkk_listings.csv")
    df = pd.read_csv(listing_data)
    return df


def get_avg_neighbourhood_price(df):
    df_filt = df.drop(df[df["price"].isna()].index)
    avg_price = (
        df_filt.groupby(by="neighbourhood", as_index=False)["price"].mean().round(2)
    )
    return avg_price


def write_data():
    get_avg_neighbourhood_price(get_data()).to_csv(
        os.path.join(os.getcwd(), "data/cal/avg_price.csv")
    )


write_data()
