from typing import Dict, List
from src.models.ner.infer import infer_entities
import random

def fpe_entities(text: str) -> str:
    entities = infer_entities(text)
    result = text
    for entity_type, entity_list in entities.items():
        for entity in sorted(entity_list, key=len, reverse=True):
            if entity in result:
                if entity_type in ["credit", "phone"]:
                    digits = [d for d in entity if d.isdigit()]
                    encrypted = ''.join(random.choice('0123456789') for _ in digits)
                    formatted = '-'.join(encrypted[i:i+4] for i in range(0, len(encrypted), 4)) if entity_type == "credit" else encrypted
                    result = result.replace(entity, formatted)
    return result