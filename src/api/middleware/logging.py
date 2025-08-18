from fastapi import Request
from typing import Callable

async def log_request(request: Request, call_next: Callable):
    """Log requests for traceability."""
    response = await call_next(request)
    return response