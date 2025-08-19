import pytest
from src.parsers.xml.parser import parse_xml
from src.schema.message import Message
from pathlib import Path

def test_parse_xml(tmp_path: Path):
    """Test XML parser with sample data."""
    xml_content = '''<?xml version="1.0"?>
        <messages>
            <message id="1" timestamp="2025-08-18" sender="user">Hello</message>
        </messages>'''
    file = tmp_path / "test.xml"
    file.write_text(xml_content, encoding='utf-8')
    messages = list(parse_xml(str(file)))
    assert len(messages) == 1
    msg = Message(**messages[0])
    assert msg.id == "1"
    assert msg.content == "Hello"
    assert msg.timestamp == "2025-08-18"
    assert msg.sender == "user"