import pandas as pd

# Read the movies.csv, tags.csv, and ratings.csv files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')

# Merge the movies, tags, and ratings dataframes
merged_df = pd.merge(movies_df, tags_df, on='movieId', how='inner')
merged_df = pd.merge(merged_df, ratings_df, on='movieId', how='inner')

# Extract the year and month from the 'timestamp' column
merged_df['year'] = pd.to_datetime(merged_df['timestamp_y'], unit='s').dt.year
merged_df['month'] = pd.to_datetime(merged_df['timestamp_y'], unit='s').dt.month_name()

# Group by year and month, calculate the average rating, and find the top category for each month and year
top_categories = merged_df.groupby(['year', 'month']).apply(lambda x: x.groupby('genres')['rating'].mean().idxmax())

# Print the list of top movie categories by month and year
for (year, month), category in top_categories.items():
    print(f"Year: {year}, Month: {month}, Top Category: {category}")
