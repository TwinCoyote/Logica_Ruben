import os


def solution_scrapper(path: str) -> str:
    '''Extract the solution and return code in str format
    Args:
        path: Path to the file
    Returns:
        str with all the code solution from the user
    '''
    resolved_path = os.path.abspath(path)

    if not os.path.exists(resolved_path):
        return ""

    with open(resolved_path, 'r', encoding="utf-8") as file:
        code = file.read()
    return code
