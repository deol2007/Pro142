import numpy as np
import pandas as pd

df = pd.read_csv('shared_articles.csv')

user_interactions = df.copy()

def total_interactions(x):
    v = x['VIEW']
    l = x['LIKE']
    b = x['BOOKMARK']
    f = x['FOLLOW']
    c = x['COMMENT CREATED']
    return (v + l + b + f + c)
user_interactions['interactions'] = user_interactions.apply(total_interactions, axis=1)

user_interactions = user_interactions.sort_values('interactions', ascending=False)
output = user_interactions[['timestamp','contentId','contentType','url','title','lang']].head(20).values.tolist()