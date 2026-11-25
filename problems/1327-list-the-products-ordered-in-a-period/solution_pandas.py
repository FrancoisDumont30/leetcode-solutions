import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df_orders = orders.loc[(orders["order_date"]<"2020-03-01") & (orders["order_date"]>="2020-02-01")]
    df_orders = df_orders.groupby(["product_id"])["unit"].sum()

    result = pd.merge(df_orders,products, on = "product_id", how="left")
    result = result.loc[(result["unit"]>=100),["product_name","unit"]].reset_index(drop=True)
    return result
