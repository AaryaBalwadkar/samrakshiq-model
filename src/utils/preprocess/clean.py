import unicodedata

def normalize_text(text: str) -> str:
    """Unicode NFC, trim, collapse whitespace."""
    text = unicodedata.normalize("NFC", text)
    text = ' '.join(text.strip().split())
    return text