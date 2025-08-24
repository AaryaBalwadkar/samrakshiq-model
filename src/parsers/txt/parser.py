from typing import Iterator
from ..common.types import MessageDict
from ...utils.preprocess.clean import normalize_text

def parse_txt(file_path: str) -> Iterator[MessageDict]:
    """Stream TXT messages, one per line with id:content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            parts = line.strip().split(":", 1)
            yield {
                "id": parts[0] if parts else str(i),
                "content": normalize_text(parts[1] if len(parts) > 1 else ""),
                "timestamp": "",
                "sender": ""
            }