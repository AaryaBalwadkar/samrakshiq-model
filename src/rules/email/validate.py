import re

def validate_email(text: str) -> bool:
    """Validate email address within text (e.g., user@example.com)."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return bool(re.search(pattern, text.lower()))