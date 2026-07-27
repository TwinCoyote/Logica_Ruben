"""Repository helpers for locating challenge files."""
from retos_cli.repository.challenge_repository import find_challenge


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
    path = f"Ejercicios_Logica/{challenge_number}_{challenge_name}"

    return path
