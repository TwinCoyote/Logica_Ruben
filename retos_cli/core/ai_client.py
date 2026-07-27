import os
from dotenv import load_dotenv

load_dotenv()

def is_debug() -> bool:
    return os.environ.get("DEBUG", "").lower() == "true"


def review_code(prompt: str) -> str:
    '''Send prompt with the code and receive response from AI client.
    Args:
        prompt: The prompt to send to AI
    Returns:
        str with JSON response containing corrections and metrics.
    '''
    if is_debug():
        return """
    {
    "score": 8.7,
    "correct": true,
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "code_quality": 8.5,
    "readability": 9.0,
    "maintainability": 8.0,
    "strengths": [
        "The algorithm is correct for the expected input.",
        "Variable names are descriptive and easy to understand."
    ],
    "bugs": [
        "The function does not validate empty input."
    ],
    "suggestions": [
        "Extract repeated logic into a helper function.",
        "Add unit tests."
    ]
    }
    """
    from google import genai
    client = genai.Client(api_key=os.environ.get("API_KEY"))
    interaction = client.interactions.create(
        model="gemini-2.0-flash", input=prompt)
    return interaction.output_text
