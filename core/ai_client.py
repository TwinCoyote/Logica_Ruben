
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ.get("API_KEY"))


def review_code(prompt: str) -> str:
    '''# Send prompt with the code and recive the response
    Args:
        prompt: Recive the answer to send AI
    Returns:
        str with the corrections and another info.
    '''

    interaction = client.interactions.create(
        model="gemini-3.5-flash", input=prompt
    )
    return interaction.output_text
