from django.contrib import admin
from .models import Profile

# admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birthday', 'city')
    list_filter = ('user', 'phone', 'birthday', 'city')
    search_fields = ('user', 'phone', 'birthday', 'city')
