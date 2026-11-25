import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    min_years = sales.groupby('product_id')['year'].transform('min')
    result = sales[sales['year'] == min_years]
    result = result.rename(columns={"year":"first_year"})
    return result[['product_id','first_year','quantity','price']]
