from models import MovieDetails
from tmdb import route
from tmdb.schema import Movie, Movies, Credits
from typing import List

genre_mapping = {
  28: "Action",
  12: "Adventure",
  16: "Animation",
  35: "Comedy",
  80: "Crime",
  99: "Documentary",
  18: "Drama",
  10751: "Family",
  14: "Fantasy",
  36: "History",
  27: "Horror",
  10402: "Music",
  9648: "Mystery",
  10749: "Romance",
  878: "Science Fiction",
  10770: "TV Movie",
  53: "Thriller",
  10752: "War",
  3: "Western",
}

def get_genre(id: int) -> str:
  return genre_mapping[id]

async def get_movie_details(title: str) -> MovieDetails:
  results = await route.Movie().search(title)
  movie_results: Movies = results.to(Movies)
  if len(movie_results.results) < 1:
    print("no movie found called {}".format(title))

  details: Movie = movie_results.results[0]
  credits_resp = await route.Movie().credits(movie_id=details.id)
  genres: List[str] = [genre_mapping[id] for id in details.genre_ids ]
  credits = credits_resp.to(Credits)
  movie_details = MovieDetails(credits=credits, movie=details, genres=genres)
  return movie_details