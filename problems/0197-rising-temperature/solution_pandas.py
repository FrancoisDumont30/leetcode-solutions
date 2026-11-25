import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
    # ensure the DataFrame is sorted by 'recordDate'
    weather.sort_values(by='recordDate', inplace=True)

    # calculate the difference in dates and temperatures between consecutive rows
    date_diff = weather['recordDate'].diff().dt.days
    temperature_diff = weather['temperature'].diff()

    # filter rows based on the conditions and return the 'id' column
    return weather[(date_diff == 1) & (temperature_diff > 0)][['id']]
