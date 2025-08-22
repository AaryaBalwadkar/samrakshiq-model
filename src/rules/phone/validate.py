import re

def validate_phone(text: str) -> bool:
    # Strict phone regex: must match a whole "word"
    pattern = re.compile(
        r'^(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}$'
    )
    
    # Split by spaces/punctuation into "words"
    words = re.findall(r'\S+', text)

    for word in words:
        # Check regex on each word separately
        if pattern.match(word):
            digits = re.sub(r'\D', '', word)  # strip non-digits
            if 10 <= len(digits) <= 15:
                print("Valid phone word:", word)
                return True
    return False