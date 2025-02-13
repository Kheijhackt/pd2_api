from django.contrib import admin
from .models import Device

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'operating', 'status', 'created', 'modified']
    search_fields = ['id']
    # For testing purposes, the fields could be edited. 
    # readonly_fields = ['operating', 'status', 'created', 'modified'] 

admin.site.register(Device, UserAdmin)