def compute_average_imdb_by_category(movies, category):
    filtered_movies = [movie for movie in movies if movie["category"] == category]
    if filtered_movies: 
        total_score = sum(movie["imdb"] for movie in filtered_movies)
        return total_score / len(filtered_movies)
    return 0