from movie import get_movie_details
from hints import get_movie_hints
import logging
from tmdb import route
from typing import Dict

async def play_game(title: str):

  logging.getLogger('asyncio').setLevel(logging.WARNING)

  b = route.Base()
  b.key = "97932f51c010e0d70823633e8105faea"

  movie_details = await get_movie_details(title)
  
  hints = get_movie_hints()
  selection_dict: Dict[int, str] = {}
  sel = 1
  for h in hints.keys():
    selection_dict[str(sel)] = h
    sel += 1
  user = 0
  while True:
    for choice in selection_dict.keys():
      print("{}: {}".format(choice, selection_dict[choice]))
    if user in selection_dict:
      hints[selection_dict[user]](movie_details)
    user = input("which hint?: ")