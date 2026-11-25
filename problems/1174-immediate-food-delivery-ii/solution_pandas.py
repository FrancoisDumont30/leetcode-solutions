import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['immediate'] = 0
    list = []
    for index, row in delivery.iterrows() :
        if row['order_date'] == row['customer_pref_delivery_date']:
            list.append(1)
        else :
            list.append(0)
    delivery['immediate'] = list

    # Obtenir les indices des premières occurrences de 'order_date' pour chaque 'customer_id'
    first_indices = delivery.groupby('customer_id')['order_date'].idxmin()

    # Sélectionner les lignes correspondantes dans le DataFrame original
    delivery = delivery.loc[first_indices]

    result = (delivery['immediate'].mean()).round(4)

    # Créer un nouveau DataFrame avec immediate_mean
    df = pd.DataFrame({'immediate_percentage': [100*result]})

    return df
