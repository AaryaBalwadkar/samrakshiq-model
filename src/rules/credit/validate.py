import re

def validate_credit(text: str) -> bool:
    """Validate credit card number within text (e.g., 4539-1234-5678-9012, 4012888888881881)."""
    pattern = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b|\b\d{13,16}\b'
    match = re.search(pattern, text)
    if not match:
        return False
    cleaned = re.sub(r'[\s-]', '', match.group())
    return len(cleaned) in (13, 15, 16) and cleaned.isdigit()