#! /usr/bin/python3

from datetime import datetime, date
import requests
from game import play_game
import json
import asyncio

token = "97932f51c010e0d70823633e8105faea"
genres = {
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

def get_genre(id: str):
  return genres[id]


def get_updated_list():
  resp = requests.get("https://framed.wtf/_next/static/chunks/872-f3ae51f095124c75.js")
  data = resp.text
  starting_index = data.find("var i=[")
  ending_index = starting_index+data[starting_index:].find("]")
  # print(data[:ending_index])
  data_part = data[starting_index:ending_index]
  data_part = data_part[6:] + "]"
  data_part = data_part.replace("title:", "\"title\":").replace("id:", "\"id\":").replace(r"\x", "")
  obj = json.loads(data_part)
  
  return obj

def get_framed_movies():
  movies = get_updated_list()
  movies_dict = {}
  for m in movies:
    movies_dict[m["id"]] = m["title"]
  
  return movies_dict

def get_todays_framed() -> str:
  some_day = date(2022, 12, 7)
  today = datetime.now().date()
  days_since = today - some_day
  movie_dict = get_framed_movies()

  index = days_since.days + 276 % len(movie_dict)
  keys = movie_dict.keys()
  max_key = max(keys)
  if index > max_key:
    index = max(index % max_key, 1)
  
  while not index in movie_dict:
    index = index + 1

  movie = movie_dict[index]
  return movie

async def main():
  title: str = get_todays_framed()
  print(title)
  await play_game(title)

asyncio.run(main())
