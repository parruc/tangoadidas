from .models import Event
from .models import Player
from .models import Team
from .models import TeamMembership
from django.contrib import admin


class TeamMembershipInline(admin.TabularInline):
    model = TeamMembership
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMembershipInline,)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
