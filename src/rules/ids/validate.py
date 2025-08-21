import re

def validate_id(text: str) -> bool:
    """Validate IDs but avoid phone numbers."""
    pattern = re.compile(
        r'\b(?:(?:ID|ref)[- ]?[A-Za-z0-9]{2,20}|[A-Za-z]{2,5}[-]?\d{2,10})\b',
        re.IGNORECASE
    )
    return bool(pattern.search(text))
