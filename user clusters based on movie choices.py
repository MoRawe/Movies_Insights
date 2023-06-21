import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Read the .csv files
movies_df = pd.read_csv('MOVIE(movieId,title,genres).csv')
tags_df = pd.read_csv('Tags(userId,movieId,tag,timestamp).csv')
ratings_df = pd.read_csv('Ratings(userId,movieId,rating,timestamp).csv')

# Merge the movies, tags, and ratings dataframes on movieId
merged_df = pd.merge(movies_df, tags_df, on='movieId', how='inner')
merged_df = pd.merge(merged_df, ratings_df, on='movieId', how='inner')

# Prepare the data for clustering
user_movie_ratings = merged_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)
scaler = MinMaxScaler()
scaled_ratings = scaler.fit_transform(user_movie_ratings.values)

# Apply K-means clustering
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_ratings)

# Add the cluster labels to the user_movie_ratings dataframe
user_movie_ratings['cluster'] = kmeans.labels_

# Analyze individual preferences
individual_preferences = user_movie_ratings.groupby('userId').mean()

# Analyze user clusters based on movie choices
cluster_preferences = user_movie_ratings.groupby('cluster').mean()

# Print the individual preferences and cluster preferences
print("Individual Preferences:")
print(individual_preferences)
print("\nCluster Preferences:")
print(cluster_preferences)
