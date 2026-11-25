import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers['num'].drop_duplicates(keep=False)
    df = df.sort_values(ascending=False)


    return pd.DataFrame({'num': [max(df, default = None)]})
