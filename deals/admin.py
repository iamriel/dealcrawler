from django.contrib import admin

from .models import (
    Company,
    Deal,
)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'company',
    ]
    list_filter = ['company']


admin.site.register(Company)
