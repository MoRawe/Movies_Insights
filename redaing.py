import pandas as pd
import matplotlib.pyplot as plt

# Read the movies.csv, tags.csv, and ratings.csv files

movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')
ratings_df = pd.read_csv('ratings.csv')


# Basic statistics
# print(ratings_df.describe())

# How well movies are liked or disliked
# print(ratings_df.value_counts())

# Let’s look at a visual representation of the data by creating a histogram
# ratings = ratings_df['rating']
# # Create the histogram plot
# ratings.hist(bins=30)
# # Display the plot
# plt.xlabel('Rating')
# plt.ylabel('Frequency')
# plt.title('Rating Distribution')
# plt.show()

movies_rating = (ratings_df
                  .set_index("movieId")
                  .join(movies_df.set_index("movieId"),
                        how="left")
                 )

print(movies_rating.head())























