import orjson
from pydantic import BaseModel, Field
from typing import Optional

class Message(BaseModel):
    """Unified schema for parsed SMS messages."""
    id: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    timestamp: Optional[str] = None
    sender: Optional[str] = None

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson.dumps