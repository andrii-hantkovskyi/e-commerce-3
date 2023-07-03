from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserCreationForm, UserChangeForm
from users.models import User, Customer


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ["email", "is_staff"]
    list_filter = ["is_staff"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_staff"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["email", "full_name", "phone_number"]
    search_fields = ["email", "first_name", "last_name", "phone_number"]
    ordering = ["user__email"]

    def email(self, obj: Customer):
        return obj.user.email

    def full_name(self, obj: Customer):
        return f'{obj.first_name} {obj.last_name}'
    full_name.short_description = 'Full name'

admin.site.unregister(Group)
