from django.contrib import admin
from .models import Highest_qualification, Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'surname', 'equity', 'phone_number', 'highest_qualification', 'email', 'next_of_keen_name', 'next_of_keen_cellphone')
    list_filter = ('course', 'equity', 'highest_qualification', 'email')
    search_fields = ('course', 'equity', 'highest_qualification', 'email', 'name')

@admin.register(Highest_qualification)
class Highest_qualificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'qualification')
    list_filter = ('id', 'qualification')
    search_fields = ('id', 'qualification')