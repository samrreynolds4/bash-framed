from tmdb.schema import Movie, Credits, Genre
from typing import List


class MovieDetails:
  credits: Credits
  movie: Movie
  genres: List[Genre]

  def __init__(self, credits: Credits, movie: Movie, genres: List[str]):
    self.credits = credits
    self.movie = movie
    self.genres = genres
