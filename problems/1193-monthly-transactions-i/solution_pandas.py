import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # Garder seulement les mois et l'année dans 'trans_date'
    transactions['trans_date'] = transactions['trans_date'].dt.strftime('%Y-%m')

    transactions['trans_count'] = 1
    transactions['approved_count'] = 0
    transactions['approved_total_amount'] = 0

    # Itération sur chaque ligne avec iterrows
    list = []
    a_amount = []
    for index, row in transactions.iterrows():
        if row['state'] == 'approved':
            list.append(1)
            a_amount.append(row['amount'])
        else :
            list.append(0)
            a_amount.append(0)
    transactions['approved_count'] = list
    transactions['approved_total_amount'] = a_amount


    # Grouper les données par 'trans_date', 'country', et 'state' et agréger
    transactions = transactions.groupby(['trans_date', 'country'], dropna=False).agg({'amount': 'sum',
    'trans_count': 'sum',
    'approved_count': 'sum',
    'approved_total_amount':'sum'
    }).reset_index()

    transactions = transactions.rename(columns={'trans_date':'month', 'amount':'trans_total_amount'})

    return transactions[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']]
