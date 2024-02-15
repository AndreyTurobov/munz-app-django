from dataclasses import dataclass
from datetime import datetime


@dataclass
class GuestEntity:
    phone: str
    create_at: datetime
