from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['code', 'weevil_detected', 'created', 'modified']
    search_fields = ['code']
    readonly_fields = ['created', 'modified']

admin.site.register(User, UserAdmin)