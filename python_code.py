# Movie Recommendation System

movies = [
    {"title": "Avatar", "genre": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "Titanic", "genre": ["Romance", "Drama"]},
    {"title": "Avengers", "genre": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "Inception", "genre": ["Action", "Sci-Fi", "Thriller"]},
    {"title": "The Notebook", "genre": ["Romance", "Drama"]},
    {"title": "Interstellar", "genre": ["Adventure", "Drama", "Sci-Fi"]},
    {"title": "John Wick", "genre": ["Action", "Thriller"]},
    {"title": "The Matrix", "genre": ["Action", "Sci-Fi"]},
    {"title": "La La Land", "genre": ["Romance", "Drama", "Music"]},
    {"title": "Gladiator", "genre": ["Action", "Drama"]}
]

# Function: Display all movies

def display_movies():
    print("\nAvailable Movies:\n")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie['title']}")
    print("\n")


# Function: Find movie by name

def find_movie(movie_name):
    for movie in movies:
        if movie["title"].lower() == movie_name.lower():
            return movie
    return None


# Function: Calculate similarity

def calculate_similarity(movie1, movie2):
    genres1 = set(movie1["genre"])
    genres2 = set(movie2["genre"])
    
    common = genres1.intersection(genres2)
    score = len(common)
    
    return score


# Function: Get recommendations

def get_recommendations(selected_movie):
    recommendations = []

    for movie in movies:
        if movie["title"] != selected_movie["title"]:
            score = calculate_similarity(selected_movie, movie)
            
            if score > 0:
                recommendations.append({
                    "title": movie["title"],
                    "score": score
                })

    return recommendations

# Function: Sort recommendations

def sort_recommendations(recommendations):
    return sorted(recommendations, key=lambda x: x["score"], reverse=True)


# Function: Display recommendations

def display_recommendations(movie_name, recommendations):
    print(f"\nTop recommendations for '{movie_name}':\n")
    
    if not recommendations:
        print("No similar movies found.")
        return

    for i, rec in enumerate(recommendations[:5], start=1):
        print(f"{i}. {rec['title']} (Similarity Score: {rec['score']})")

# Main Program

def main():
    print("🎬 Welcome to Movie Recommendation System 🎬")
    
    while True:
        print("\n1. Show all movies")
        print("2. Get recommendations")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            movie_name = input("Enter movie name: ")
            selected_movie = find_movie(movie_name)

            if not selected_movie:
                print("Movie not found. Please try again.")
                continue

            recommendations = get_recommendations(selected_movie)
            sorted_recs = sort_recommendations(recommendations)
            display_recommendations(movie_name, sorted_recs)

        elif choice == "3":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()