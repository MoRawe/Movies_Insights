import pandas as pd

# Read the movies.csv, tags.csv, and ratings.csv files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')

# Merge the movies and tags dataframes based on the movieId column
merged_df = pd.merge(movies_df, tags_df, on='movieId')

# Merge the merged_df with ratings_df based on the movieId column
merged_df = pd.merge(merged_df, ratings_df, on='movieId')

# Calculate the total number of ratings per genre
genre_ratings = merged_df.groupby('genres')['rating'].count()

# Sort the genres based on the total number of ratings in descending order
sorted_genres = genre_ratings.sort_values(ascending=False)

# Print the top 6 genres by the total number of ratings
top_genres = sorted_genres.head(6)
print(top_genres)
