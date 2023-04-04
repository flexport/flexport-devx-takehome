"""
    Copyright 2023 Flexport International, LLC

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import json


from flask import Flask, request

from .rps import rock_paper_scissors


class InvalidMove(Exception):
    """
    Invalid Move
    """


app = Flask(__name__)


@app.route("/health")
def health():
    """
    Returns OK if the server is running.
    """
    return "OK"


@app.route("/rps", methods=["POST"])
def rps():
    """
    Plays a round of rock-paper-scissors against the computer.
    Expects a JSON object with a "move" key specifying the player's move.
    Returns a JSON object with the result of the game.
    """
    # Create number to choice mapping
    mapping = ["Rock", "Paper", "Scissors"]

    move = request.json.get("move", "")
    try:
        user_choice = mapping.index(move.lower().capitalize())
    except ValueError:
        raise InvalidMove(f"{move} is invalid. Valid moves: {mapping}") from None

    game_result, pc_choice = rock_paper_scissors(user_choice)
    if game_result == 0:
        result = "Tie"
    elif game_result == -1:
        result = f"I win, {mapping[pc_choice]} beats {move}"
    else:
        result = f"You win, {move} beats {mapping[pc_choice]}"

    return json.dumps(
        {"result": result, "game_result": game_result, "pc_choice": pc_choice}
    )
