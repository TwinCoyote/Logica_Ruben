import json


def json_to_dict(json_response: str) -> dict:
    """Parse JSON response string into dictionary.
    Args:
        json_response: The text to convert
    Returns:
        The dict
    """
    response = json.loads(json_response)
    return response
