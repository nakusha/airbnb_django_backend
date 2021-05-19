from . import models
from django.contrib import admin


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
    pass
