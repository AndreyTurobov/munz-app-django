from django.http import HttpRequest
from ninja import Router

from core.api.v1.coins.schemas import CoinListSchema


router = Router(tags=['Coins'])


@router.get('', response=CoinListSchema)
def get_coin_list_handler(request: HttpRequest) -> CoinListSchema:
    return []