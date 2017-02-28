# from django import forms
from .models import Event
from .models import Player
from .models import PlayerPointsInEvent
from .models import Team
from django.contrib import admin


# from easy_maps.widgets import AddressWithMapWidget

class PlayerPointsInEventInline(admin.TabularInline):
    model = PlayerPointsInEvent
    extra = 1


# class EventAdminForm(forms.ModelForm):
#    class Meta:
#        model = Event
#        fields = '__all__'
#        widgets = {
#            'place': AddressWithMapWidget
#        }


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">supervisor_account</i>'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # form = EventAdminForm
    icon = '<i class="material-icons">schedule</i>'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = (PlayerPointsInEventInline, )
    icon = '<i class="material-icons">person_pin</i>'
