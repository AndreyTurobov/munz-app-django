from dataclasses import dataclass
from datetime import datetime


@dataclass
class Coin:
    id: int  # noqa
    title: str
    description: str
    country: str
    issue_at: str
    state: str
    created_at: datetime
    updated_at: datetime
