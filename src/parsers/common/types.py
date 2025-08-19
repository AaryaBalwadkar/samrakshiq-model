from typing import Dict, Iterator, Optional
from pydantic import BaseModel

class Message(BaseModel):
    """Unified message schema for parsing."""
    id: str
    content: str
    timestamp: Optional[str] = None
    sender: Optional[str] = None

MessageDict = Dict[str, str]
MessageIterator = Iterator[MessageDict]