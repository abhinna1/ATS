# Application Tracking System

This is an ATS project that analyzes a CV provided in PDF format using Gemini models provided by Google.

## Installation

### Install dependencies

Simply run `pip install -r requirements.txt` after activating your venv.

### Set environment variables

Run `cp .sample.env .env`. Then populate the environment variables in the .env file.

### Run the main.py file.

## Contributing

In order to contribute, you need to first setup pre-commit and ruff.

Run `pre-commit install` to install pre-commit into your git hooks. This will automatically trigger the ruff-format command when you make a commit.
