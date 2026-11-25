import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby('reports_to').agg(reports_count=('name','count'),average_age=('age','mean')).reset_index()
    df = df.rename(columns={'reports_to':'employee_id'})
    employees = employees.merge(df, on='employee_id', how='left')

    employees = employees.loc[employees['reports_count'].notnull()]
    employees['average_age'] = (employees['average_age']+0.001).round()

    return employees[['employee_id','name','reports_count','average_age']].sort_values(by='employee_id')
