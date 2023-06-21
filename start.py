import pandas as pd

# Read the movies.csv, tags.csv, and ratings.csv files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')

# print(movies_df.head())
# print(movies_df.head(59))
# print(movies_df.tail(10))
# print(movies_df.describe())
# print(tags_df['tag'].value_counts())
print(movies_df['genres'].value_counts())

