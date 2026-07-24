# pylint: disable = E0401,W0401,C0403,W0611,C0413,C0412,C0114,W0511,E0602,W0718



import sys
from pathlib import Path
from google.genai import errors

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

PARENT_DIR = Path(__file__).resolve().parent.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.insert(0, str(PARENT_DIR))

from parse_response import json_to_dict
from ai_client import review_code
from build_prompt import build_prompt
from extract_solution import solution_scrapper
from repository.file_repository import find_challenge_file
from ui.reporter import *

try:
    from repository.challenge_repository import find_challenge
except ImportError:  # pragma: no cover - fallback for direct script execution
    from challenge_repository import find_challenge


def review_challenge(challenge_number: int):
    """# Return the review using the functions from all file
    Args:
        challenge_number: The number from the file to review
    Returns: The feedback from the solve challenge

    """
    try:
        name_path = find_challenge_file(challenge_number)
        path = f"../../{name_path}.py"

        solution = solution_scrapper(path)

        prompt = build_prompt(solution)

        review = review_code(prompt)

        analysis = json_to_dict(review)

        show_info = show_review(analysis)

        return show_info
    except errors.APIError as e:
        show_general_error(e)
    except Exception as e:
        show_general_error(e)


# print(review_challenge(27))
