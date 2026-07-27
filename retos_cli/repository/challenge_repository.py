import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHALLENGES_PATH = os.path.abspath(os.path.join(
    BASE_DIR, "..", "..", "data", "Retos_programacion.json"))


def find_challenge(number: int) -> dict:
    '''Find a challenge from JSON catalog and return info dictionary.
        Args:
            number: The number of the challenge.
        Returns:
            The challenge info dict.
    '''
    if not os.path.exists(CHALLENGES_PATH):
        return {}

    with open(CHALLENGES_PATH, "r", encoding="utf-8") as challenges:
        challenge = json.load(challenges)
        number_str = str(number)
        try:
            challenge_info = {
                "number": int(number),
                "name": challenge[number_str]["name"],
                "dificulty": challenge[number_str]["dificulty"],
                "description": challenge[number_str]["description"]
            }
            return challenge_info
        except KeyError:
            return {}
