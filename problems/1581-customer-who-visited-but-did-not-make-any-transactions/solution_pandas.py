import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(visits, transactions, on ="visit_id", how="outer")
    df = df.fillna(0)
    df = df.loc[df["transaction_id"]== 0,:]
    df = df.groupby(["customer_id"])["transaction_id"].count().reset_index()
    df = df.rename({"transaction_id":"count_no_trans"}, axis=1)
    
    return df
