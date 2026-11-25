import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema.loc[cinema['description']!='boring']
    cinema = cinema.loc[cinema['id']%2!=0]
    return cinema.sort_values('rating', ascending=False)
