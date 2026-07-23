from ai_client import review_code
from build_prompt import build_prompt
from extract_solution import solution_scrapper
from repository.challenge_repository import find_challenge


def review_challenge(challenge_number: int):
    """# Return the review using the functions from all file
    Args:
        challenge_number: The number from the file to review
    Returns: The feedback from the solve challenge

    """
    path = ""

    find_challenge()
    solution_scrapper()
    build_prompt()
    review_code()
    # TODO: parse_response()
    # TODO: reporter()
