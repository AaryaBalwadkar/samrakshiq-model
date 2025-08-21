import re

def validate_credit(text: str) -> bool:
    """Validate credit card number within text (13–16 digits)."""
    # Supports formats like: 4539-1234-5678-9012, 4012 8888 8888 1881, 5105105105105100
    pattern = r'(?:\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b|\b\d{13,16}\b)'
    match = re.search(pattern, text)
    if not match:
        return False

    cleaned = re.sub(r'[\s-]', '', match.group())
    return cleaned.isdigit() and 13 <= len(cleaned) <= 16
