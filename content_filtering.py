import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('shared_articles.csv')

def create_soup(x):
    return ' '.x['TITLE']

df['soup'] = df.apply(create_soup, axis=1)
df['soup'].lower()

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df = df.reset_index()
indices = pd.Series(df.index, index=df['title'])

def get_recommendations(contentId, cosine_sim):
  idx = indices[contentId]
  contentID = list(enumerate(cosine_sim[idx]))
  contentID = sorted(contentID, key=lambda x: x[1], reverse=True)
  contentID = contentID[1:11]
  article_indices = [i[0] for i in contentID]
  return df['title'].iloc[article_indices]