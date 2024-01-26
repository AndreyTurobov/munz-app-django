from django.contrib import admin

from core.apps.coins.models.coins import Coin


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'title', 
        'country', 
        'description', 
        'state',
        )
