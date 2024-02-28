from django.contrib.auth import get_user_model
from django.contrib import admin

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email'
    )
