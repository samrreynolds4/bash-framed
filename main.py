import asyncio
from game import play_game
import logging

logging.getLogger('aiohttp').setLevel(logging.WARNING)



async def main():
  await play_game("The Godfather")

asyncio.run(main())