import json


def json_to_dict(json_response: str) -> dict:
    """# Returns the Json response to dict
    Args:
        input:
            Input he text to convert
    Returns:
        The dict 
    """
    responce = json.loads(json_response)
    return responce
