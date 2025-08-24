import orjson
from typing import Iterator
from ..common.types import MessageDict
from ...utils.preprocess.clean import normalize_text

def parse_json(file_path: str) -> Iterator[MessageDict]:
    """Stream JSON messages from array or objects."""
    with open(file_path, 'rb') as f:
        data = orjson.loads(f.read())
        messages = data if isinstance(data, list) else [data]
        for msg in messages:
            yield {
                "id": str(msg.get("id", "")),
                "content": normalize_text(msg.get("content", "")),
                "timestamp": msg.get("timestamp", ""),
                "sender": msg.get("sender", "")
            }