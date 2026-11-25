import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:


    transactions = transactions.groupby(["account"])["amount"].sum()
    result = pd.merge(users,transactions,how="left",on="account")
    result = result.loc[result["amount"]>10000,:]
    result = result.rename({"amount":"balance"}, axis=1)
    result = result.iloc[:, 1:3]
    return result
