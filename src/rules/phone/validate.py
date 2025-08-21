import re

def validate_phone(text: str) -> bool:
    """Detect phone numbers inside text (10–15 digits with optional separators)."""
    pattern = re.compile(
        r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}'
    )
    matches = pattern.findall(text)
    for match in matches:
        digits = re.sub(r'\D', '', match)  # strip non-digits
        if 10 <= len(digits) <= 15:
            return True
    return False

