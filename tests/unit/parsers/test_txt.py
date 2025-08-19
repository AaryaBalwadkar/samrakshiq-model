import pytest
from src.parsers.txt.parser import parse_txt
from src.schema.message import Message
from pathlib import Path

def test_parse_txt(tmp_path: Path):
    """Test TXT parser with sample data."""
    txt_content = "1:Hello"
    file = tmp_path / "test.txt"
    file.write_text(txt_content, encoding='utf-8')
    messages = list(parse_txt(str(file)))
    assert len(messages) == 1
    msg = Message(**messages[0])
    assert msg.id == "1"
    assert msg.content == "Hello"
    assert msg.timestamp is None
    assert msg.sender is None