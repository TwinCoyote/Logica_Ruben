import ast
from textwrap import dedent

# * Succes


def show_succes(x: tuple[str, str, str]) -> None:
    '''# Print a succes message with the path on the console'''
    print(f"✔ {x[1]}\n")
    print(f"Ruta:\n{x[2]}")
    return None

# * Error


def show_error(x: tuple[str, int]) -> None:
    '''Print a error message with the number on the console.'''
    print(f"✖ El reto {x[1]} no existe.")
    return None


def show_general_error(x: str) -> None:
    '''Print a error message with the number on the console.'''
    error_text = str(x)
    payload = error_text.split(" - ", 1)[1].rstrip(".")
    error_data = ast.literal_eval(payload)
    print(f"✖ {error_data["error"]["message"]}.")
    return None


# * Info


def show_info(msg: str) -> None:
    '''Print a custom message like info'''
    print(f"{msg}...")
    return None


# * Analysis

def show_review(dic: dict):
    """Print the review from Ai"""

    top = f"""
    =====================================
                Review Report
    =====================================

⭐ Score:                    {dic.get("score")}

✅ Correct:                  {dic.get('time_complexity')}

💾 Space Complexity:         {dic.get("time_complexity")}

📊 Code Quality:             {dic.get("code_quality")}

📖 Readability:              {dic.get("readability")}

🛠 Maintainability:           {dic.get("maintainability")}
    """

    strengths = "\n".join(f"✔ {x}" for x in dic.get("strengths", []))
    bugs = "\n".join(f"✖ {x}" for x in dic.get("bugs", []))
    suggestions = "\n".join(f"→  {x}" for x in dic.get("suggestions", []))

    lists = f"""
Strengths
__________

{strengths}

Potential Bugs
_______________

{bugs}

Suggestions
-----------

{suggestions}

"""

    output = f"""
    {top}

    {lists}
    
    
    """

    return output



