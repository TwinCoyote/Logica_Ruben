# Retos CLI

A command-line tool that automates programming challenge creation and provides AI-powered code reviews.

## Features

- Generate Python files for programming challenges from a numbered catalog
- Create exercise templates automatically in a dedicated folder (`Ejercicios_Logica/`)
- Review solutions with AI-powered feedback using Google Gemini
- Centralized challenge catalog in JSON format

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Retos-CLI
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   # .venv\Scripts\activate   # On Windows
   ```

3. Install the package in editable mode with dependencies:

   ```bash
   pip install -e .
   ```

4. Set your API key in your environment or `.env` file:
   ```bash
   export API_KEY="your_api_key_here"
   ```

## Usage

Generate a challenge file:

```bash
reto create 27
```

Review a solution for a specific challenge:

```bash
reto review 27
```

Alternatively, you can run the module directly with Python:

```bash
python -m retos_cli.cli create 27
python -m retos_cli.cli review 27
```

## Architecture

The project follows a modular Python package architecture:

```
Retos-CLI/
│
├── retos_cli/
│   ├── __init__.py
│   ├── cli.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── create.py
│   │   ├── review.py
│   │   ├── ai_client.py
│   │   ├── build_prompt.py
│   │   ├── extract_solution.py
│   │   └── parse_response.py
│   ├── repository/
│   │   ├── __init__.py
│   │   ├── challenge_repository.py
│   │   └── file_repository.py
│   └── ui/
│       ├── __init__.py
│       └── reporter.py
│
├── data/
│   └── Retos_programacion.json
│
├── tests/
│   ├── __init__.py
│   └── test_cli.py
│
├── pyproject.toml
└── README.md
```

## Running Tests

Run unit tests with `unittest`:

```bash
python -m unittest discover -s tests
```

## Technologies

- Python 3.10+
- JSON for challenge data
- Google Gemini API for automated code review
- `python-dotenv` for environment variable management
- `setuptools` for packaging and CLI entrypoint

## License

This project is currently unlicensed.
