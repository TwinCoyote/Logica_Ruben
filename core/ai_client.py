# pylint: disable = E0401,C0403,W0611,C0413,C0412,C0114,W0511,E0402
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


Debug = os.environ.get("DEBUG", "").lower() == "true"


def review_code(prompt: str) -> str:
    '''# Send prompt with the code and recive the response
    Args:
        prompt: Recive the answer to send AI
    Returns:
        str with the corrections and another info.
    '''
    
    if Debug:
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
    client = genai.Client(api_key=os.environ.get("API_KEY"))
    
    interaction = client.interactions.create(
        model="gemini-2.0-flash", input=prompt)
    return interaction.output_text
