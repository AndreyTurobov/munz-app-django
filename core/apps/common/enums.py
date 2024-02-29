from enum import Enum


class EntityStatus(Enum):
    NOT_LOADED = 'not_loaded'
    LOADING = 'loading'
    LOADED = 'loaded'
