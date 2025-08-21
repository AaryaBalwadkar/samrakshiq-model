from typing import Dict, List
from src.models.ner.infer import infer_entities

def redact_entities(text: str) -> str:
    entities = infer_entities(text)
    result = text
    for entity_type, entity_list in entities.items():
        for entity in sorted(entity_list, key=len, reverse=True):
            if entity in result:
                result = result.replace(entity, "[REDACTED]")
    return result