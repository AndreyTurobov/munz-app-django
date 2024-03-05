from functools import lru_cache

import punq

from core.apps.coins.services.coins import (
    BaseCoinService,
    ORMCoinService,
)
from core.apps.coins.services.reviews import (
    BaseReviewService,
    BaseReviewValidatorService,
    ComposedReviewValidatorService,
    ORMReviewService,
)
from core.apps.coins.use_cases.reviews.create import CreateReviewUseCase
from core.apps.guests.services.auth import (
    AuthService,
    BaseAuthService,
)
from core.apps.guests.services.codes import (
    BaseCodeService,
    DjangoCacheCodeService,
)
from core.apps.guests.services.guests import (
    BaseGuestService,
    ORMGuestService,
)
from core.apps.guests.services.senders import (
    BaseSenderService,
    ComposedSenderService,
    EmailSenderService,
    PushSenderService,
)


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # initialize coins
    container.register(BaseCoinService, ORMCoinService)

    # initialize guests
    container.register(BaseGuestService, ORMGuestService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    container.register(
        BaseSenderService,
        ComposedSenderService,
        sender_services=(
            PushSenderService(),
            EmailSenderService(),
        ),
    )
    container.register(BaseAuthService, AuthService)

    container.register(BaseReviewService, ORMReviewService)
    container.register(
        BaseReviewValidatorService,
        ComposedReviewValidatorService,
        validators=[],
    )
    container.register(CreateReviewUseCase)

    return container
