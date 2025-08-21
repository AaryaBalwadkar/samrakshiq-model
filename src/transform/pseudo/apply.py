from typing import Dict, List
from src.models.ner.infer import infer_entities
from uuid import uuid4

_pseudo_map = {}

def pseudonymize_entities(text: str) -> str:
    entities = infer_entities(text)
    result = text
    for entity_type, entity_list in entities.items():
        for entity in sorted(entity_list, key=len, reverse=True):
            if entity in result:
                pseudo_id = str(uuid4())[:8]
                _pseudo_map[entity] = pseudo_id
                result = result.replace(entity, f"[{entity_type.upper()}_PSEUDO:{pseudo_id}]")
    return result