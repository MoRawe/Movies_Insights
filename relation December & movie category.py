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

# Filter the data for December only
december_data = merged_df[merged_df['month'] == 'December']

# Group by year and movie category, calculate the average rating, and find the top category for each year
top_categories_december = december_data.groupby('year').apply(lambda x: x.groupby('genres')['rating'].mean().idxmax())

# Print the list of highest rating movie categories in December for each year
for year, category in top_categories_december.items():
    print(f"Year: {year}, Highest Rating Category in December: {category}")
