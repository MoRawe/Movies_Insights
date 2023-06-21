import pandas as pd

# Read the .csv files
movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')

# Merge the movies and tags dataframes on movieId
merged_df = pd.merge(movies_df, tags_df, on='movieId', how='inner')

# Define negative words
negative_words = ['bad', 'terrible', 'awful', 'horrible', 'disappointing', 'dark', 'not funny', 'sad']
positive_words = ['good', 'excellent', 'awesome', 'fantastic', 'great', 'funny', 'quirky']


# Filter tags containing negative words
negative_tags = merged_df[merged_df['tag'].str.contains('|'.join(negative_words), case=False)]
positive_tags = merged_df[merged_df['tag'].str.contains('|'.join(positive_words), case=False)]


# Group by movie category and count the number of negative tags
category_negative_counts = negative_tags.groupby('genres').size()
category_positive_counts = positive_tags.groupby('genres').size()

# Print each movie category with the number of negative words
# for category, count in category_negative_counts.items():
#     print(f"Movie Category: {category}, Negative Words Count: {count}")
for category, count in category_positive_counts.items():
    print(f"Movie Category: {category}, Positive Words Count: {count}")