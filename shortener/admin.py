from django.contrib import admin
from .models import LinkShortener


@admin.register(LinkShortener)
class LinkShortenerAdmin(admin.ModelAdmin):
    search_fields = ('long_url',)
    list_display = ('__str__', 'active')
    list_filter = ('created', 'updated')
