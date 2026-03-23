import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load Dataset
# -----------------------------
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!\n")
        return data
    except:
        print("Error loading dataset.")
        return None

# -----------------------------
# Preprocess Data
# -----------------------------
def preprocess_data(data):
    print("Preprocessing data...\n")
    
    # Combine genre and description
    data['content'] = data['genre'] + " " + data['description']
    
    return data

# -----------------------------
# Vectorization
# -----------------------------
def vectorize_text(data):
    print("Vectorizing text using TF-IDF...\n")
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(data['content'])
    
    return tfidf_matrix, vectorizer

# -----------------------------
# Compute Similarity
# -----------------------------
def compute_similarity(tfidf_matrix):
    print("Computing similarity matrix...\n")
    
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    return similarity_matrix

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_movies(movie_title, data, similarity_matrix):
    
    if movie_title not in data['title'].values:
        print("Movie not found in dataset.")
        return
    
    print(f"\nRecommendations for '{movie_title}':\n")
    
    # Get index of movie
    idx = data[data['title'] == movie_title].index[0]
    
    # Get similarity scores
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    
    # Sort movies based on similarity
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Skip first one (itself)
    similarity_scores = similarity_scores[1:6]
    
    for i, score in similarity_scores:
        print(f"{data.iloc[i]['title']} (Score: {round(score, 2)})")

# -----------------------------
# Display All Movies
# -----------------------------
def show_movies(data):
    print("Available Movies:\n")
    for movie in data['title']:
        print("-", movie)
    print("\n")

# -----------------------------
# Main Program
# -----------------------------
def main():
    data = load_data("movies.csv")
    
    if data is None:
        return
    
    data = preprocess_data(data)
    
    tfidf_matrix, vectorizer = vectorize_text(data)
    
    similarity_matrix = compute_similarity(tfidf_matrix)
    
    while True:
        show_movies(data)
        
        user_input = input("Enter a movie you like (or 'exit'): ")
        
        if user_input.lower() == 'exit':
            print("Exiting program...")
            break
        
        recommend_movies(user_input, data, similarity_matrix)
        
        print("\n" + "-"*40 + "\n")

# Run program
if __name__ == "__main__":
    main()