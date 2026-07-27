from retos_cli.core.parse_response import json_to_dict
from retos_cli.core.ai_client import review_code
from retos_cli.core.build_prompt import build_prompt
from retos_cli.core.extract_solution import solution_scrapper
from retos_cli.repository.file_repository import find_challenge_file
from retos_cli.ui.reporter import show_review, show_general_error


def review_challenge(challenge_number: int):
    """Review a challenge solution using AI.
    Args:
        challenge_number: The number of the challenge file to review
    Returns:
        Formatted review string or error report.
    """
    try:
        name_path = find_challenge_file(challenge_number)
        if not name_path:
            return f"✖ El reto {challenge_number} no existe."

        path = f"{name_path}.py"

        solution = solution_scrapper(path)
        if not solution:
            return f"✖ No se encontró el archivo de solución en {path}."

        prompt = build_prompt(solution)

        review = review_code(prompt)

        analysis = json_to_dict(review)

        show_info = show_review(analysis)

        return show_info
    except Exception as e:
        show_general_error(e)
        return str(e)
