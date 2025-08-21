import hashlib
from typing import Dict, List
from src.models.ner.infer import infer_entities

def hash_entities(text: str) -> str:
    entities = infer_entities(text)
    result = text
    for entity_type, entity_list in entities.items():
        for entity in sorted(entity_list, key=len, reverse=True):
            if entity in result:
                hashed = hashlib.sha256(entity.encode()).hexdigest()
                result = result.replace(entity, f"[{entity_type.upper()}_HASH:{hashed[:8]}]")
    return result