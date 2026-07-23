import os


def solution_scrapper(path: str) -> str:
    '''# Extract the solution and return a code in str format
    Args:
        path: Path from the file
    Returns:
        str with all the code solution from the user
    '''
    base_dir = os.path.dirname(__file__)
    resolved_path = path if os.path.isabs(
        path) else os.path.abspath(os.path.join(base_dir, path))

    if not os.path.exists(resolved_path):
        return ""

    with open(resolved_path, 'r', encoding="utf-8") as file:
        code = file.read()
    return code
