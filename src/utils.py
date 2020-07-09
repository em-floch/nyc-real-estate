from src.params import DATA_PATH, os
import pandas as pd
import pickle as pkl


def save_df(df, filename):
    path = os.path.join(DATA_PATH, f"{filename}.csv")
    df.to_csv(path)


def save_pkl(df, filename):
    path = os.path.join(DATA_PATH, f"{filename}.pkl")
    pkl.dump(df, open(path, 'wb'))


def load_pkl_or_csv(filename):
    paths = {ext: os.path.join(DATA_PATH, f"{filename}.{ext}")
             for ext in ['pkl', 'csv']}
    try:
        if os.path.exists(paths['pkl']):
            df = pickle.load(open(paths['pkl'], "rb"))
        elif os.path.exists(paths['csv']):
            df = pd.read_csv(paths['csv'])
    except IOError:
        raise FileNotFoundError
