import pandas as pd

# Read the CSV files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')

# Merge movies and tags dataframes on movieId
merged_df = pd.merge(movies_df, tags_df, on='movieId', how='inner')

# Group by genre and count the number of tags
genre_tag_counts = merged_df.groupby('genres').size().reset_index(name='tag_count')

# Group by genre and calculate the average rating
genre_avg_ratings = ratings_df.merge(movies_df, on='movieId', how='inner').groupby('genres')['rating'].mean().reset_index(name='average_rating')

# Merge tag counts and average ratings by genre
genre_data = pd.merge(genre_tag_counts, genre_avg_ratings, on='genres', how='inner')

# Sort genres based on the combined popularity metric (tag count and average rating)
genre_data['popularity'] = genre_data['tag_count'] * genre_data['average_rating']
popular_genres = genre_data.sort_values('popularity', ascending=False)

# Print the top 3 popular genres
top_3_genres = popular_genres.head(3)
print("Top 3 Popular Genres:")
for _, row in top_3_genres.iterrows():
    print(f"Genre: {row['genres']}, Popularity: {row['popularity']}")