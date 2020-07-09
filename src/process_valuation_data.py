import pandas as pd
import datadotworld as dw
import os
from src.params import DATA_URL, DATA_PATH
from src.utils import load_df, save_df


def load_data(filename="prop_valuation.csv"):
    try:
        df = load_pkl_or_csv("prop_valuation")
        return df
    except FileNotFoundError:
        df = pd.read_csv(DATA_URL)
        save_pkl(df, "prop_valuation")
        return df
