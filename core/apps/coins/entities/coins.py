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
    create_at: datetime
    update_at: datetime
