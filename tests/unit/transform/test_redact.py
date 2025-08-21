import pytest
from src.transform.redact.apply import redact_entities
from src.models.ner.infer import infer_entities

real_messages = [
    "SBI Alert: Your UPI txn to +919876543210 is successful. Ref ID: UPI-123456.",
    "HDFC Bank: Suspicious activity on card 4111-1111-1111-1111.",
    "Edge case: +9198 (invalid phone) and ID: ID-12 (short ID) with 412345678901234 (long card).",
    "Multiple: Call +918765432109 and +919223344556, email test@domain.in, ID: MULTI-123.",
]

@pytest.mark.parametrize("text", real_messages)
def test_redact_entities(text):
    redacted = redact_entities(text)
    entities = infer_entities(text)
    print(f"Original: {text}")
    print(f"Redacted: {redacted}")
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            assert "[REDACTED]" in redacted, f"Entity {entity} not redacted in {redacted}"
    assert len(redacted.split()) <= len(text.split()), "Redaction increased word count unexpectedly"