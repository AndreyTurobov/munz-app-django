from ninja import Router

from core.api.v1.coins.handlers import router as coin_router
from core.api.v1.guests.handlers import router as guest_router
from core.api.v1.reviews.handlers import router as review_router


router = Router(tags=['v1'])

coin_router.add_router('', review_router)

router.add_router('guests/', guest_router)
router.add_router('coins/', coin_router)
