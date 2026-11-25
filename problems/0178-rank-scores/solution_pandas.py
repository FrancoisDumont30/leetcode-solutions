import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    data = scores.sort_values("score", ascending=False).reset_index(drop=True)
    data["rank"]=1
    data2 = data[["score", "rank"]]
    
    for n in range (0,data2.shape[0]):
        if n == 0:
            pass
        elif data2["score"][n] == data2["score"][n-1] :
            data2["rank"][n] = data2["rank"][n-1]
        else :
            data2["rank"][n] = (data2["rank"][n-1])+1
        
        
    return data2
