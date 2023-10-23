def movie_organizer(*args):
    genres = {}

    for films in args:
        film_name, genre = films

        if genre not in genres:
            genres[genre] = []

        genres[genre].append(film_name)

    sorted_genres = sorted(genres.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    output = ""

    for genre, movies in sorted_genres:
        output += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            output += f"* {movie}\n"

    return output.strip()
