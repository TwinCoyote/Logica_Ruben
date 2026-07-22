import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHALLENGES_PATH = os.path.abspath(os.path.join(
    BASE_DIR, "..", "data", "Retos_programacion.json"))


def find_challenge(number: int) -> dict:
    '''# Find a from json and return a object
        Args:
            number: The number of the challenge.
        Returns:
            The challenge info in order of objects.
    '''

    with open(CHALLENGES_PATH, "r", encoding="utf-8") as challenges:
        challenge = json.load(challenges)
        number = str(number)
        try:
            challenge_info = {
                "number": int(number),
                "name": challenge[number]["name"],
                "dificulty": challenge[number]["dificulty"],
                "description": challenge[number]["description"]
            }
            return challenge_info
        except KeyError:
            return {}


# print(find_challenge(9))
