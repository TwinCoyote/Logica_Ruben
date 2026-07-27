import ast
from textwrap import dedent

# * Success


def show_succes(x: tuple[str, str, str]) -> None:
    '''Print a success message with the path on the console'''
    print(f"✔ {x[1]}\n")
    print(f"Ruta:\n{x[2]}")
    return None

# * Error


def show_error(x: tuple[str, int]) -> None:
    '''Print an error message with the challenge number.'''
    print(f"✖ El reto {x[1]} no existe.")
    return None


def show_general_error(x: Exception | str) -> None:
    '''Print a general error message.'''
    error_text = str(x)
    msg = error_text
    try:
        parts = error_text.split(" - ", 1)
        if len(parts) > 1:
            payload = parts[1].rstrip(".")
            error_data = ast.literal_eval(payload)
            if isinstance(error_data, dict) and "error" in error_data:
                msg = error_data["error"].get("message", error_text)
    except Exception:
        pass

    try:
        print(f"✖ {msg}")
    except UnicodeEncodeError:
        print(f"[X] {msg}")
    return None


# * Info


def show_info(msg: str) -> None:
    '''Print a custom info message.'''
    print(f"{msg}...")
    return None


# * Analysis

def show_review(dic: dict):
    """Print the review from AI"""

    top = f"""
    =====================================
                Review Report
    =====================================

⭐ Score:                    {dic.get("score")}

✅ Correct:                  {dic.get('correct')}

⏱️ Time Complexity:          {dic.get('time_complexity')}

💾 Space Complexity:         {dic.get("space_complexity")}

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
