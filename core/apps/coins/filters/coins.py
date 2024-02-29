from dataclasses import dataclass


@dataclass(frozen=True)
class CoinFilters:
    search: str | None = None
