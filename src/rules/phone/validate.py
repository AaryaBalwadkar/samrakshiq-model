import re

def validate_phone(text: str) -> bool:
    """Validate phone number by stripping separators and checking digit length."""
    cleaned = re.sub(r'[\(\) -.\s]', '', text.strip())
    if cleaned.startswith('+'):
        cleaned = cleaned[1:]
    return cleaned.isdigit() and 10 <= len(cleaned) <= 15