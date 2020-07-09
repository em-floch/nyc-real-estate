import pytest
import pandas as pd
from src.process_data import load_data


def test_load_data():
    df = load_data()

    assert isinstance(df, pd.DataFrame)
