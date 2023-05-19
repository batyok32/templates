from django.contrib import admin

# from .forms import UserCreationForm
from .models import User
from django.contrib.auth.admin import UserAdmin


class UseAdmin(UserAdmin):
    list_display = ["id", "username"]
    # add_form = UserCreationForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_superuser",
                    "is_active",
                    "is_staff",
                    "user_permissions",
                    "groups",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )


admin.site.register(User, UseAdmin)
