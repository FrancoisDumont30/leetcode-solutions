import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["count"] = queries.query_name.map(queries.query_name.value_counts())
    queries['percentage'] = (queries['rating'] < 3) * 100
    queries["quality"] = queries.rating/queries.position + 1e-6
    queries["poor_query_percentage"]=queries['percentage']/queries["count"]
    queries = queries.groupby(["query_name"]).agg({"quality":"mean","poor_query_percentage":"sum"}).round(2).reset_index()
    
    return queries
