from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Contact Information', {'fields': ('name', 'email', 'phone')}),
        ('Message', {'fields': ('message',)}),
        ('Metadata', {'fields': ('created_at',)}),
    )