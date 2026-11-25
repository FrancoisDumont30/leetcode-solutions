import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    a = employee.managerId.value_counts()
    return employee.loc[employee['id'].isin(a[ a >= 5 ].index), ['name']]
