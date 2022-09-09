import json
from flask import Flask, jsonify, request
from models import GetGamesFilters, VideoGame
from mongo_repository import MongoRepository
from games_usecase import GamesUsecase

app = Flask(__name__)

### This PART SHOULD BE ISOLATED IN GLOBAL APP CREATION PART

# USE ENVIRONMENT VARIABLES INSTEAD TO LEAD CONF
MONGO_URI = "mongodb://localhost:27017/"

mongo_client = MongoRepository(MONGO_URI)
games_usecase = GamesUsecase(mongo_client)


@app.route("/games", methods=["GET"])
def get_games():
    filters = GetGamesFilters(request.args)
    games = games_usecase.list_games(filters)
    return jsonify({"games": games}), 200


@app.route("/games", methods=["POST"])
def add_game():
    ## Parse Data in our models
    data = json.loads(request.data)

    try:
        new_game = VideoGame(**data)
    except Exception as e:
        return jsonify({"msg": f"Failed to Add Game: {e}"}), 400

    games_usecase.add_game(game=new_game)

    return jsonify({"msg": "sucess"}), 201


@app.route("/games/<game_id>", methods=["PUT"])
def update_game(game_id):
    return "<p>Hello, World!</p>", 200


@app.route("/games/<game_id>", methods=["DELETE"])
def delete_game(game_id):
    return "<p>Hello, World!</p>", 200
