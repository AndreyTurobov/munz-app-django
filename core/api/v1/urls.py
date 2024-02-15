from ninja import Router

from core.api.v1.coins.handlers import router as coin_router
from core.api.v1.guests.handlers import router as guest_router


router = Router(tags=['v1'])
router.add_router('coins/', coin_router)
router.add_router('guests/', guest_router)
