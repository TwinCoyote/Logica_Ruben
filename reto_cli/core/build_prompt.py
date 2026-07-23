

def build_prompt(code: str) -> str:
    '''# Generate a prompt using the code received

    Args:
        code:
            code received from the program
    Returns:
        the complete prompt
    '''

    json_structure = """
    {
    "score": 0.0,
    "correct": true,
    "time_complexity": "",
    "space_complexity": "",
    "code_quality": 0.0,
    "readability": 0.0,
    "maintainability": 0.0,
    "strengths": [],
    "bugs": [],
    "suggestions": []
    }
    """

    prompt = f"""
    You are a Senior Software Engineer specialized in Python, algorithms, software architecture, and technical code reviews.

    Your task is to review the source code provided below as if you were reviewing a Pull Request from a junior developer.

    Evaluate the solution according to the following criteria:

    1. Functional correctness
    2. Algorithm efficiency
    3. Time complexity
    4. Space complexity
    5. Code quality
    6. Readability
    7. Maintainability
    8. Python best practices
    9. Potential bugs
    10. Edge cases that may fail

    Base your evaluation on software engineering best practices rather than personal preferences. Do not be overly strict, but do not ignore important problems.

    The response must be valid JSON that can be parsed directly using Python's json.loads().

    Do NOT include:
    - Markdown
    - Code fences
    - Explanations before or after the JSON
    - Any additional text

    If a field cannot be determined, use null instead of inventing information.
    Do not invent bugs if none exist.
    Do not invent strengths if none exist.
    Be objective.
    
    The JSON must have EXACTLY the following structure:

    {json_structure}

    Now review the following source code:

    ==================== CODE ====================

    {code}

    ================== END CODE ==================

    """

    return prompt


print(build_prompt("xdxdxdxdxd"))
