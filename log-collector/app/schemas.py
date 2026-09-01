from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class LogEvent(BaseModel):
    timestamp: datetime
    service: str
    environment: str = "development"
    level: str
    eventType: str
    traceId: str | None = None
    userId: str | None = None
    requestId: str | None = None
    message: str
    metadata: dict[str, Any] = Field(default_factory=dict)