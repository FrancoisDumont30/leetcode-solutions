import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    num_player = activity['player_id'].nunique()
    first_log = activity.groupby('player_id')['event_date'].min().reset_index(name='first_log')
    activity = activity.merge(first_log, how='left', on='player_id')

    activity['event_date'] = pd.to_datetime(activity['event_date'])
    activity['first_log'] = pd.to_datetime(activity['first_log'])
    activity = activity.loc[activity['event_date'] == (activity['first_log'] + pd.to_timedelta(1, unit='d'))]

    result = [round((len(activity)/num_player),2)]

    df = pd.DataFrame(result, columns=['fraction'])

    return df
