import pytest
from src.models.obfuscate.detect import obfuscate_entities
from src.models.ner.infer import infer_entities

real_messages = [
    "URGENT: Your package is delayed. Track with +918123456789 or email track@shipfast.in. Ref: PK-4567.",
    "Win $1000! Reply YES to claims@winlottery.org or call 1-800-555-1234. ID: W-7890.",
    "Bank alert: Suspicious activity on 4123-4567-8912-3456. Contact support@securebank.com.",
]

@pytest.mark.parametrize("text", real_messages)
def test_obfuscate_entities(text):
    entities = infer_entities(text)
    obfuscated = obfuscate_entities(text, entities)
    print(f"Original: {text}")
    print(f"Obfuscated: {obfuscated}")
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            assert f"[{entity_type.upper()}_MASK]" in obfuscated, f"Entity {entity} not masked with [{entity_type.upper()}_MASK] in {obfuscated}"