from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI

from core.api.schemas import PingResponseSchema
from core.api.v1.urls import router as v1_router


api = NinjaAPI(title=['MunzApp_API'])


@api.get("/ping", response=PingResponseSchema, tags=['development'])
def ping(request: HttpRequest) -> PingResponseSchema:
    return PingResponseSchema(result=True)


api.add_router('v1/', v1_router)

urlpatterns = [
    path("", api.urls),
]
