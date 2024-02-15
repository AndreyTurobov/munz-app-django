from django.contrib import admin

from core.apps.guests.models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone',
        'create_at',
    )
