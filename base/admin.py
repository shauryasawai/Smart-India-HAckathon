
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import KnowledgeLevel


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
admin.site.register(CustomUser, CustomUserAdmin)

class KnowledgeLevelAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'level')  # Ensure these are valid fields

admin.site.register(KnowledgeLevel, KnowledgeLevelAdmin)
