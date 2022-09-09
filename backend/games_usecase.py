from mongo_repository import MongoRepository
from models import GetGamesFilters, VideoGame


class GamesUsecase:
    def __init__(self, games_db: MongoRepository) -> None:
        # Inject the Mongo Client
        self.games_db = games_db

    def list_games(self, filters: GetGamesFilters):
        "Query Games in the DB"
        # Handling of filters step

        return self.games_db.get_games(filters)

    def add_game(self, game: VideoGame) -> str:
        "Create a Game and return its ID"
        return self.games_db.add_game(game)

    def delete_game(self, game_id: str):
        pass

    def update_game(self, game_id: str, game: VideoGame):
        pass
