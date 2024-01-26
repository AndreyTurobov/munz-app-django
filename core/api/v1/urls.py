from ninja import Router

from core.api.v1.coins.handlers import router as coin_router


router = Router(tags=['v1'])
router.add_router('coins/', coin_router)
