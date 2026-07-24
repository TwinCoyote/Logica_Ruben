"""Repository helpers for locating challenge files."""
# pylint: disable = E0401,C0403,W0611,C0413,C0412,C0114,W0511,E0402
import os
import sys

if __package__ in {None, ""}:
    ROOT_DIR = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir))
    if ROOT_DIR not in sys.path:
        sys.path.insert(0, ROOT_DIR)
    from repository.challenge_repository import find_challenge
else:
    from .challenge_repository import find_challenge


def find_challenge_file(challenge_number: int) -> str | None:
    """
    Find a challenge file using the challenge number.

    Args:
        challenge_number: Number of the challenge.

    Returns:
        The path to the challenge file if it exists, otherwise ``None``.
    """
    challenge = find_challenge(challenge_number)
    if not challenge:
        return None
    challenge_name = challenge.get("name")
    path = f"Ejercicios_Logica/{challenge_number}-{challenge_name}"

    return path


# print(find_challenge_file(27))
