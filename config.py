import logging
import os

from dotenv import load_dotenv

load_dotenv()

# OpenAI API credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_ENGINE = os.getenv("OPENAI_MODEL_ENGINE")

# Model parameters
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS"))
OPENAI_N = int(os.getenv("OPENAI_N"))
OPENAI_STOP = os.getenv("OPENAI_STOP")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE"))

# Logging configuration
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"

# Set up logging
logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)
