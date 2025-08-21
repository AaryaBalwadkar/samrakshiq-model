import pytest
import re
from src.models.ner.infer import infer_entities

real_messages = [
    "URGENT: Your package is delayed. Track with +918123456789 or email track@shipfast.in. Ref: PK-4567.",
    "Win $1000! Reply YES to claims@winlottery.org or call 1-800-555-1234. ID: W-7890.",
    "Bank alert: Suspicious activity on 4123-4567-8912-3456. Contact support@securebank.com.",
    "Pay toll fee now: $25 due. Call +441234567890 or ID: TOL-1234.",
    "Crypto tip: Buy BTC via invest@coinpro.com. Card: 5105-1051-0510-5100."
]

@pytest.mark.parametrize("text", real_messages)
def test_infer_entities(text):
    entities = infer_entities(text)
    assert all(re.search(r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}', e) for e in entities["phone"]) or not any(re.search(r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}', text))
    assert all(re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', e) for e in entities["email"]) or not any(re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))
    assert all(re.search(r'\b(?:(?:ID|ref)[- ]?[A-Za-z0-9]{2,20}|[A-Za-z]{2,5}[-]?\d{2,10})\b', e, re.IGNORECASE) for e in entities["id"]) or not any(re.search(r'\b(?:(?:ID|ref)[- ]?[A-Za-z0-9]{2,20}|[A-Za-z]{2,5}[-]?\d{2,10})\b', text, re.IGNORECASE))
    assert all(re.search(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b|\b\d{13,16}\b', e) for e in entities["credit"]) or not any(re.search(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b|\b\d{13,16}\b', text))