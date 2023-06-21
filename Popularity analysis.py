import pandas as pd

# Read the CSV files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')

# Count the number of tags for each movie
tag_counts = tags_df.groupby('movieId').size().reset_index(name='tag_count')

# Calculate the average rating for each movie
average_ratings = ratings_df.groupby('movieId')['rating'].mean().reset_index(name='average_rating')

# Merge tag counts and average ratings with movies dataframe
movies_data = pd.merge(movies_df, tag_counts, on='movieId', how='left')
movies_data = pd.merge(movies_data, average_ratings, on='movieId', how='left')

# Sort movies based on the combined popularity metric (tag count and average rating)
movies_data['popularity'] = movies_data['tag_count'] * movies_data['average_rating']
popular_movies = movies_data.sort_values('popularity', ascending=False)

# Print the top 10 popular movies
top_10_movies = popular_movies.head(10)
print("Top 10 Popular Movies:")
for _, row in top_10_movies.iterrows():
    print(f"Movie ID: {row['movieId']}, Title: {row['title']}, Popularity: {row['popularity']}")

