from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "phone_number", "country")
    search_fields = ("username", "email", "phone_number")
