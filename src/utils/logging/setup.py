import structlog
from typing import Any

def setup_logger(level: str = "INFO") -> Any:
    """Configure structlog for performance."""
    structlog.configure(
        processors=[structlog.processors.TimeStamper(fmt="iso")],
        logger_factory=structlog.PrintLoggerFactory()
    )
    return structlog.get_logger(level=level)