import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    df = sales.set_index('product_id').join(product.set_index('product_id')).reset_index()


    df = df[['product_name', 'year', 'price']]
    return df
