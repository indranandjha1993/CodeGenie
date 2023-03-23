import argparse
import logging
import re

import openai
from dotenv import load_dotenv

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL_ENGINE,
    OPENAI_MAX_TOKENS,
    OPENAI_N,
    OPENAI_STOP,
    OPENAI_TEMPERATURE,
    LOGGING_LEVEL,
    LOGGING_FORMAT,
)

load_dotenv()

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)
logger = logging.getLogger(__name__)

openai.api_key = OPENAI_API_KEY
model_engine = OPENAI_MODEL_ENGINE
max_tokens = OPENAI_MAX_TOKENS
n = OPENAI_N
stop = OPENAI_STOP
temperature = OPENAI_TEMPERATURE


def generate_code(prompt, location=None):
    logger.info(f"Generating code for prompt: {prompt}")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        stop=stop,
        temperature=temperature,
    )
    message = completions.choices[0].text
    message = message.replace("\n", "").strip()
    pattern = r"\b\d+\b"
    matches = re.findall(pattern, message)
    for match in matches:
        message = message.replace(match, f"int({match})")
    logger.info(f"Generated code: {message}")
    if location:
        with open(location, "w") as f:
            f.write(message)
            logger.info(f"Code written to file: {location}")
    else:
        filename = "generated_code.py"
        with open(filename, "w") as f:
            f.write(message)
            logger.info(f"Code written to file: {filename}")
    return message


def main():
    parser = argparse.ArgumentParser(description="Generate Python code using OpenAI's GPT-3")
    parser.add_argument("prompt", help="The prompt to use for code generation")
    parser.add_argument(
        "-l",
        "--location",
        help="The location to save the generated code (default: generated_code.py in the current directory)",
    )
    args = parser.parse_args()
    generate_code(args.prompt, args.location)


if __name__ == "__main__":
    main()
