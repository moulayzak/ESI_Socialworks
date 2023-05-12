from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "username","creation_date", "is_staff", "is_active",)
    list_filter = ("email", "username","creation_date", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email","username", "phone_number", "address", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "phone_number", "address","creation_date", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, CustomUserAdmin)
class BAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Fund, BAdmin)
admin.site.register(Program, BAdmin)
admin.site.register(Chapter, BAdmin)
admin.site.register(Division, BAdmin)
admin.site.register(Request, BAdmin)
admin.site.register(Transaction, BAdmin)
admin.site.register(Event,BAdmin)

admin.site.register(Notification,BAdmin)

