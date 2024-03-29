# gpt-service

## Overview

This is a simple Flask-based API that utilizes OpenAI's GPT-3.5 for text generation. It provides endpoints for generating text based on user input.

## Dependencies

Make sure to install the required dependencies before running the API.

- Flask (2.0.1)
- OpenAI (0.27.0)
- Werkzeug (2.0,< 3.0)
- Pytest (7.1.3)

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Setting up the Environment

It's recommended to use a virtual environment to manage the project dependencies. Here are the basic steps to set up the environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
.\venv\Scripts\activate

# Activate the virtual environment (Unix or MacOS)
source venv/bin/activate
```

## Running the API

To run the API, use the following command:

```bash
python run.py
```

The API will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

- **POST /generate-text**
  - Generates text based on user input.
  - Request JSON format:
    ```json
    {
        "input_text": "Your input text here."
    }
    ```
  - Response JSON format:
    ```json
    {
        "generated_text": "Generated text output."
    }
    ```

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## Deactivating the Virtual Environment

To deactivate the virtual environment, use the following command:

```bash
deactivate
```
