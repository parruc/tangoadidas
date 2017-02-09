from django.contrib import admin

from .models import Event
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
