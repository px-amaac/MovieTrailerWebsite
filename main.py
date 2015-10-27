import media
import fresh_tomatoes
import json

# open the movies.json file that I have created
file = open('movies.json', 'r')

# create a new array to hold my movie items
movie_items = []

# create a dict from the json file.
movies = json.load(file)

# iterate throigh the movies json, create instances of the movie items and add them to the movieItems list.
for movie in movies:
    movie_items.append(media.Movie(
        movie["title"],
        movie["poster_image_url"],
        movie["trailer_youtube_url"],
        movie["running_time"],
        movie["release_date"]
    ))

fresh_tomatoes.open_movies_page(movie_items)
