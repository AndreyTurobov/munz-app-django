from django.contrib import admin

from core.apps.coins.models.coins import Coin
from core.apps.coins.models.reviews import Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'country',
        'description',
        'state',
    )
    inlines = (ReviewInline,)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'guest',
        'text',
        'rating',
        'coin',
    )
    list_filter = ('coin',)
    list_select_related = (
        'guest',
        'coin',
    )
