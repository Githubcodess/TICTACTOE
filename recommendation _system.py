import numpy as np
import pandas as pd

# Sample user-item matrix (User ratings for Movies)
data = {
    'User': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Movie_1': [5, 4, np.nan, 2, 1],
    'Movie_2': [3, 5, 4, np.nan, 2],
    'Movie_3': [4, np.nan, 5, 4, 3],
    'Movie_4': [np.nan, 2, 1, 5, 4],
    'Movie_5': [2, 1, 2, 4, np.nan]
}

df = pd.DataFrame(data).set_index('User')

# Function to calculate Pearson correlation between users
def pearson_correlation(user1, user2):
    common_items = ~user1.isna() & ~user2.isna()
    if common_items.sum() == 0:
        return 0  # No common items
    
    user1_common = user1[common_items]
    user2_common = user2[common_items]
    
    return np.corrcoef(user1_common, user2_common)[0, 1]

# Get recommendations for a target user
def get_recommendations(df, target_user, num_recommendations=3):
    user_ratings = df.loc[target_user]
    other_users = df.drop(target_user)
    
    # Calculate similarity between target user and other users
    similarities = other_users.apply(lambda x: pearson_correlation(user_ratings, x), axis=1)
    
    # Weighted sum of ratings based on similarity
    weighted_ratings = pd.Series(0, index=df.columns)
    similarity_sum = pd.Series(0, index=df.columns)
    
    for user, similarity in similarities.items():
        if similarity > 0:  # Only consider positive correlations
            weighted_ratings += df.loc[user].fillna(0) * similarity
            similarity_sum += (df.loc[user].notna()) * similarity
    
    # Avoid dividing by zero
    similarity_sum = similarity_sum.replace(0, np.nan)
    
    # Predicted ratings for target user
    predicted_ratings = weighted_ratings / similarity_sum
    
    # Recommend items that the target user hasn't rated yet
    recommendations = predicted_ratings[user_ratings.isna()].sort_values(ascending=False).head(num_recommendations)
    
    return recommendations

# Example: Recommend movies for Alice
recommendations = get_recommendations(df, target_user='Alice')
print(f"Recommendations for Alice:\n{recommendations}")
