import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    customer['prod_total'] = product.shape[0]
    customer = customer.loc[customer['product_key']==customer['prod_total']]
    return customer[['customer_id']]
