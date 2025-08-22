import re

def validate_email(text: str) -> bool:
    """Validate if text contains an email address."""
    pattern = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+$'
    return bool(re.search(pattern, text.lower()))
