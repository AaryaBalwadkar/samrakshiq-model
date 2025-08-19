import pytest
from src.parsers.json.parser import parse_json
from src.schema.message import Message
from pathlib import Path

def test_parse_json(tmp_path: Path):
    """Test JSON parser with sample data."""
    json_content = '[{"id": "1", "content": "Hello", "timestamp": "2025-08-18", "sender": "user"}]'
    file = tmp_path / "test.json"
    file.write_text(json_content, encoding='utf-8')
    messages = list(parse_json(str(file)))
    assert len(messages) == 1
    msg = Message(**messages[0])
    assert msg.id == "1"
    assert msg.content == "Hello"
    assert msg.timestamp == "2025-08-18"
    assert msg.sender == "user"