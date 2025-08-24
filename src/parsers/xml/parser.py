from xml.etree.ElementTree import iterparse
from typing import Iterator
from ..common.types import MessageDict
from ...utils.preprocess.clean import normalize_text

def parse_xml(file_path: str) -> Iterator[MessageDict]:
    """Stream XML messages with <message> tags."""
    for _, elem in iterparse(file_path, events=("end",)):
        if elem.tag == "message":
            yield {
                "id": elem.get("id", ""),
                "content": normalize_text(elem.text or ""),
                "timestamp": elem.get("timestamp", ""),
                "sender": elem.get("sender", "")
            }
            elem.clear()