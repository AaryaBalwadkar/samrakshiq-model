import csv
from typing import Iterator
from ..common.types import MessageDict
from utils.preprocess.clean import normalize_text

def parse_csv(file_path: str) -> Iterator[MessageDict]:
    """Stream CSV messages with id,content,timestamp,sender."""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {
                "id": row.get("id", ""),
                "content": normalize_text(row.get("content", "")),
                "timestamp": row.get("timestamp", ""),
                "sender": row.get("sender", "")
            }