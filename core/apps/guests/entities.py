from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime


@dataclass
class Guest:
    id: int | None = field(default=None, kw_only=True)  # noqa
    phone: str
    create_at: datetime
