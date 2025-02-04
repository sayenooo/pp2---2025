def compute_average_imdb(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)