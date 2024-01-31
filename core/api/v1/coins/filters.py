from ninja import Schema


class CoinFilters(Schema):
    search: str | None = None
