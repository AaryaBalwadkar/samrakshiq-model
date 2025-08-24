import pytest
from src.parsers.csv.parser import parse_csv
from src.schema.message import Message
from pathlib import Path

def test_parse_csv(tmp_path: Path):
    """Test CSV parser with sample data."""
    csv_content = "id,content,timestamp,sender\n1,Hello,2025-08-18,user"
    file = tmp_path / "test.csv"
    file.write_text(csv_content, encoding='utf-8')
    messages = list(parse_csv(str(file)))
    assert len(messages) == 1
    msg = Message(**messages[0])
    assert msg.id == "1"
    assert msg.content == "Hello"
    assert msg.timestamp == "2025-08-18"
    assert msg.sender == "user"