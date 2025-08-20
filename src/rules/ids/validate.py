import re

def validate_id(text: str) -> bool:
    """Validate generic ID within text (e.g., ID-7890, A12345, B4567, ET-123456)."""
    pattern = r'(?:ID|ref)?\s*[A-Za-z][A-Za-z0-9\-]{2,19}'
    return bool(re.search(pattern, text))