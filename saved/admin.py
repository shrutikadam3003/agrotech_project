from django.contrib import admin
from .models import SavedItem

@admin.register(SavedItem)
class SavedItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'added_at')
    list_filter = ('category', 'user')
    search_fields = ('title',)