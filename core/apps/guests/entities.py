from dataclasses import dataclass
from datetime import datetime


@dataclass
class Guest:
    phone: str
    create_at: datetime
