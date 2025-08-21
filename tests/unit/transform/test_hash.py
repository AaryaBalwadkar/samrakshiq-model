import pytest
from src.transform.hash.apply import hash_entities
from src.models.ner.infer import infer_entities

real_messages = [
    "ICICI: Update via +918765432109. Email icici@update.in.",
    "Paytm: Transaction with 4123-4567-8912-3456 failed.",
    "Edge case: Email test@.in (invalid) and ID: ID-1 (short) with 123456789012 (short card).",
    "Multiple: Phone +919990001122, email support@india.in, ID: MULTI-456, card 4500123456789012.",
]

@pytest.mark.parametrize("text", real_messages)
def test_hash_entities(text):
    hashed = hash_entities(text)
    entities = infer_entities(text)
    print(f"Original: {text}")
    print(f"Hashed: {hashed}")
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            assert f"[{entity_type.upper()}_HASH:" in hashed, f"Entity {entity} not hashed in {hashed}"
    assert all(f"_HASH:" in hashed for _ in entities.values() if _), "No hashes detected"