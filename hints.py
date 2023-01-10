from tmdb.schema import Movie
from models import MovieDetails
from tmdb import route
from random import randint, shuffle
from typing import Dict, Callable, List

Hint = Callable[[Movie], None]

def print_release_date(movie: MovieDetails):
  print(movie.movie.release_date)

def print_genres(movie: MovieDetails):
  print([c for c in movie.genres])

def print_actors(movie: Movie):
  # print(movie.credits.__dict__)
  print([c.name for c in movie.credits.cast[:5]])

def print_characters(movie: MovieDetails):
  print([c.character for c in movie.credits.cast[:5]])

def prompt_title(title: str):
  title_words = title.split()
  title_words_arr = [['-' for c in word] for word in title_words]
  random_word_choices: List[int] = [i for i in range(len(title_words)) for _ in range(len(title_words[i]))]
  random_letter_indexes: List[List[int]] = [[i for i in range(len(word))] for word in title_words]
  for i in range(len(random_letter_indexes)):
    shuffle(random_letter_indexes[i])
  shuffle(random_word_choices)
  
  while len(random_word_choices) > 0:
    input("press enter to add a new character...")
    word_arr_index: int = random_word_choices.pop()
    letter_index: int = random_letter_indexes[word_arr_index].pop()

    title_words_arr[word_arr_index][letter_index] = title_words[word_arr_index][letter_index]
    print("    ".join(["".join([c for c in word]) for word in title_words_arr]))
  

def print_movie_title(movie: MovieDetails):
  title: str = movie.movie.name
  prompt_title(title)
  
def get_movie_hints() -> Dict[str, Hint]:
  return {
    "release date": print_release_date,
    "genres": print_genres,
    "actors": print_actors,
    "characters": print_characters,
    "title": print_movie_title,
  }

