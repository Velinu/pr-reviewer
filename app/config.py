import os
from dotenv import load_dotenv

load_dotenv()

class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass

class Config:
    GITHUB_TOKEN: str | None = os.getenv("GITHUB_TOKEN")
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")

    if not GITHUB_TOKEN:
        raise ConfigError("GITHUB_TOKEN environment variable not set.")
    if not GEMINI_API_KEY:
        raise ConfigError("GEMINI_API_KEY environment variable not set.")