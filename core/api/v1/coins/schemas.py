from datetime import datetime

from pydantic import BaseModel


class CoinSchema(BaseModel):
    title: str
    description: str
    create_at: datetime
    update_at: datetime | None = None
    
    
CoinListSchema = list[CoinSchema]
