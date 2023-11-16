import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    try:
        if not os.path.exists(path):
            raise AssertionError("The file doesnt exist")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file is not a .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        #print(load("life_expectancy_years.csv"))

        return dataset
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None