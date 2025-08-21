from typing import Dict, List

def obfuscate_entities(text: str, entities: Dict[str, List[str]]) -> str:
    result = text
    for entity_type, entity_list in entities.items():
        for entity in sorted(entity_list, key=len, reverse=True):
            if entity in result:
                result = result.replace(entity, f"[{entity_type.upper()}_MASK]")
    return result