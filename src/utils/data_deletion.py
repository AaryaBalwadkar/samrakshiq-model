from typing import Dict, Any

def delete_data(data: Dict[str, Any]) -> None:
    if data:
        for key in list(data.keys()):
            data[key] = None
            del data[key]
    return None