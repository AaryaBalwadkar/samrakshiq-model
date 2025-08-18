from dotenv import load_dotenv
from typing import Dict
import os

def load_env() -> Dict[str, str]:
    """Load .env variables securely."""
    load_dotenv()
    return {
        "ENCRYPTION_KEY": os.getenv("ENCRYPTION_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO")
    }