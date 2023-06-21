import pandas as pd

# Read the .csv files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')

# Merge the movies, tags, and ratings dataframes on movieId
merged_df = pd.merge(movies_df, tags_df, on='movieId', how='inner')
merged_df = pd.merge(merged_df, ratings_df, on='movieId', how='inner')

# Split the genres into separate columns
genres = merged_df['genres'].str.get_dummies('|')

# Concatenate the binary genre columns with the original dataframe
merged_df = pd.concat([merged_df, genres], axis=1)

# Analyze correlations between genres, tags, and ratings
correlations = merged_df.drop(['movieId', 'timestamp_y'], axis=1).corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlations)
