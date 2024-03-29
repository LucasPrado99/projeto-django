from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone', 'show',
    search_fields = 'id', 'first_name', 'last_name',
    list_editable = 'show',
    list_per_page = 10
    list_max_show_all = 100

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_per_page = 10
    list_max_show_all = 100