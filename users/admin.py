from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# @를 사용하지않고 하는방법
# admin.site.register(models.User, CustomUserAdmin)
# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthDay",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
