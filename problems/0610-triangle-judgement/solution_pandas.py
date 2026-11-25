import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = None
    test = []
    for index, row in triangle.iterrows():
        list = []
        list.append(abs(row['x']))
        list.append(abs(row['y']))
        list.append(abs(row['z']))
        list.sort()

        a = list[0]
        b = list[1]
        c = list[2]

        if (a + b > c) and (a + c > b) and (b + c > a):
            test.append('Yes')
        else :
            test.append('No')

    triangle['triangle'] = test

    return triangle
