import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df2 = customer.loc[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())]
    return df2[['name']]
