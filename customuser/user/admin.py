from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

admin.site.register(CustomUser,UserAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User role",
            {
                'fields' : (
                    'Developer',
                    'Tester',
                )
            }
        )
    )


