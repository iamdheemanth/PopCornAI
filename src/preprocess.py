import os
import pandas as pd

base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_directory = os.path.join(base_directory, 'data')

def load_datasets():
    movies = pd.read_csv(os.path.join(data_directory, 'movies.csv'))
    ratings = pd.read_csv(os.path.join(data_directory, 'ratings.csv'))
    return movies, ratings

def preprocess_datasets(movies, ratings):
    ratings.drop(['timestamp'], axis=1, inplace=True)
    data = pd.merge(ratings, movies, on='movieId')
    return data

def save_preprocessed_datasets(data):
    data.to_csv(os.path.join(data_directory, 'preprocessed_data.csv'), index=False)

if __name__ == '__main__':
    movies, ratings = load_datasets()
    preprocessed_data = preprocess_datasets(movies, ratings)
    save_preprocessed_datasets(preprocessed_data)
    print("Preprocessing complete! Find preprocessed dataset at 'data/preprocessed_data.csv'")
