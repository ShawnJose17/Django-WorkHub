from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "first_name", "last_name", "user_type", "phone", "is_staff", "is_superuser")
    list_filter = ("user_type", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("user_type", "phone"),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("user_type", "phone"),
        }),
    )

admin.site.register(User, CustomUserAdmin)
