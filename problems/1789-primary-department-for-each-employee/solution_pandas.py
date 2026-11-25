import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    dfyes = employee.loc[employee['primary_flag']=='Y']
    dfno = employee.loc[~employee['employee_id'].isin(dfyes['employee_id'])]

    dfno = dfno.drop_duplicates(subset='employee_id', keep=False)


    df = pd.concat([dfyes, dfno]) 	
    df.sort_values(by='employee_id')

    return df[['employee_id','department_id']]
