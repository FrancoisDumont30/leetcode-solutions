import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(person, address, on="personId", how="left")    
    data2 = data[["firstName", "lastName", "city", "state"]]
    return data2
