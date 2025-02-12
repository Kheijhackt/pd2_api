from django.contrib import admin
from .models import Device

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'operating', 'status', 'created', 'modified']
    search_fields = ['id']
    readonly_fields = ['operating', 'status', 'created', 'modified']

admin.site.register(Device, UserAdmin)