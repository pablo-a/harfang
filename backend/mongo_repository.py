"""
This Repository aims to handle every interaction with MongoDB.
"""

from pymongo import MongoClient
from models import VideoGame
from dataclasses import asdict

client = MongoClient()

DB = "harfang"
VIDEO_GAME_COLLECTION = "games"


class MongoRepository:
    def __init__(self, mongo_uri) -> None:
        ## Inject Mongo URI so that you could use any DB with the Repo.
        self.client = MongoClient(mongo_uri)
        self.db = self.client[DB]
        self.games = self.db[VIDEO_GAME_COLLECTION]

    def get_games(self):
        data = self.games.find()
        # Parse with models to manipulate our classes
        return data

    def add_game(self, game: VideoGame) -> str:
        "Take a Game, insert it in Mongo and return its ID"
        return self.games.insert_one(asdict(game)).inserted_id

    def update_game(self, game_id: str, game: VideoGame):
        pass

    def delete_game(self, game_id: str):
        pass
