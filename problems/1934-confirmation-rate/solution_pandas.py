import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    confirmations = confirmations.replace('confirmed', 1)
    confirmations = confirmations.replace('timeout', 0)
    confirmations = confirmations.groupby('user_id')['action'].mean().round(2).reset_index(name='confirmation_rate')
    
    confirmations = confirmations.merge(signups, on='user_id', how='outer')
    confirmations = confirmations.fillna(0)


    return confirmations[['user_id','confirmation_rate']]
