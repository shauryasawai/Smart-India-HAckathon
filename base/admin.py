
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active') 
    list_filter = ('is_staff', 'is_active', 'interests')  # Add filter options
    ordering = ('username',)  # Default ordering

    # Specify fields to include in the admin form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('interests', 'initial_score')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('interests', 'initial_score')}),
    )

# Register the custom user model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
