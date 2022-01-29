from django.contrib import admin
from .models import Device

# admin.site.register(Device)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'lendee', 'lender')
    list_filter = ('name', 'make')
    search_fields = ('name', 'make', 'lendee')