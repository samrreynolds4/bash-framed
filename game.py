from movie import get_movie_details
from hints import get_movie_hints
import logging
from tmdb import route

async def play_game(title: str):

  logging.getLogger('asyncio').setLevel(logging.WARNING)

  b = route.Base()
  b.key = "97932f51c010e0d70823633e8105faea"

  movie_details = await get_movie_details(title)
  
  hints = get_movie_hints()

  for hint in hints.values():
    input("press enter for a hint...")
    hint(movie_details)