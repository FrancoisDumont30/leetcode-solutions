import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:    
    # Jointure des DataFrames sur product_id
    merged_df = pd.merge(prices, units_sold, how='left', on='product_id')

    # Filtrer les lignes où purchase_date se trouve entre start_date et end_date
    filtered_df = merged_df[(merged_df['purchase_date'] >= merged_df['start_date']) & (merged_df['purchase_date'] <= merged_df['end_date'])]

    # Agréger les unités vendues par product_id, start_date, end_date
    units_aggregated = filtered_df.groupby(['product_id', 'start_date', 'end_date'], as_index=False)['units'].sum()

    # Joindre les unités agrégées avec le DataFrame prices
    final_df = pd.merge(prices, units_aggregated, how='left', on=['product_id', 'start_date', 'end_date'])

    # Remplacer les valeurs NaN par 0 dans la colonne units
    final_df['units'] = final_df['units'].fillna(0).astype('Int64')
    
    final_df['total'] = final_df['price'] * final_df['units']
    final_df = final_df.groupby('product_id').agg({'total': 'sum', 'units': 'sum'}).reset_index()
    final_df['average_price'] = (final_df['total']/final_df['units'])
    final_df['average_price'] = final_df['average_price'].apply(lambda x: round(x, 2))
    final_df = final_df.fillna(0)

    return final_df[['product_id', 'average_price']]
