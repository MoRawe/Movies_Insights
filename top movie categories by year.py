import pandas as pd

# Read the movies.csv, tags.csv, and ratings.csv files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')

# Merge the movies, tags, and ratings dataframes
merged_df = pd.merge(movies_df, tags_df, on='movieId', how='inner')
merged_df = pd.merge(merged_df, ratings_df, on='movieId', how='inner')

# Extract the year from the 'timestamp' column
merged_df['year'] = pd.to_datetime(merged_df['timestamp_y'], unit='s').dt.year

# Group by year and movie category, calculate the average rating, and find the top category for each year
top_categories = merged_df.groupby('year').apply(lambda x: x.groupby('genres')['rating'].mean().idxmax())

# Print the list of top movie categories by year
for year, category in top_categories.items():
    print(f"Year: {year}, Top Category: {category}")
