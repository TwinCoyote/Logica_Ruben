# Retos CLI

A command-line tool that automates programming challenge creation and provides AI-powered code reviews.

## Features

- Generate Python files for programming challenges from a numbered catalog
- Create exercise templates automatically in a dedicated folder
- Review solutions with AI-powered feedback using Google Gemini
- Keep challenge data centralized in JSON format

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd LogicaProgramacion
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install python-dotenv google-genai
   ```

4. Set your API key in your environment:
   ```bash
   set API_KEY=your_api_key_here
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

If you are running it directly from the source folder, you can also use:

```bash
python cli.py create 27
python cli.py review 27
```

## Architecture

The project is organized into a small modular structure:

- `core/`: contains the main logic for creating challenge files and reviewing solutions
- `repository/`: handles access to challenge data and file lookup
- `ui/`: manages console output and reporting
- `data/`: stores the challenge catalog in JSON format
- `config/`: contains configuration-related files

```
Retos-CLI
│
├── core/
├── repository/
├── ui/
├── data/
├── config/
└── cli.py

```


## Technologies

- Python
- JSON for challenge data
- Google Gemini API for automated code review
- dotenv for environment variable management

## Roadmap

- PostgreSQL statistics
- Local AI providers (Ollama)
- Multi-language support
- PyPI package
- GitHub Actions CI/CD
- Unit tests

## License

This project is currently unlicensed. If you want to publish or share it publicly, consider adding a LICENSE file.
