from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from app.models import Event, ProfileToEvents
from bot.models import Profile

User = get_user_model()

admin.site.unregister(User)  # если она была автоматически зарегистрирована
admin.site.unregister(Group)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "short_description", "location", "datetime", "participants_requirements", "quantity", "cover", "participants")
    search_fields = ("id", "title", "description", "short_description", "location", "datetime", "participants_requirements", "quantity", "cover")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("tg_id", "username", "first_name", "last_name")
    search_fields = ("tg_id", "username", "first_name", "last_name")

@admin.register(ProfileToEvents)
class ProfileToEventsAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    search_fields = ("id", "username")