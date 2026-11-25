import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    employee["manager_salary"] = employee['managerId'].map(employee.set_index('id')['salary'])

    employee = employee.loc[employee["salary"]>employee["manager_salary"],:]

    return employee.rename({"name":"Employee"}, axis=1).reset_index(drop=True)[["Employee"]]
