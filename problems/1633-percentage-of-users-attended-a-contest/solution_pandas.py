import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:

    result = register.groupby('contest_id')['contest_id'].value_counts().reset_index(name='percentage')
    result['percentage'] = (100*(result['percentage']/users.shape[0]))
    result['percentage'] = result['percentage'].round(2)

    return result.sort_values(by=['percentage','contest_id'], ascending=[False, True])
