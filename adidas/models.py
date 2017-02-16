from __future__ import unicode_literals
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(AbstractUser):
    is_leader = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Giocatore"
        verbose_name_plural = "Giocatori"
        db_table = 'auth_user'


class Event(models.Model):
    title = models.CharField("Titolo", max_length=128)
    date = models.DateField("Data")
    time = models.TimeField("Ora")
    place = models.TextField("Luogo")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField("Nome", max_length=128)
    event = models.ForeignKey(Event)
    members = models.ManyToManyField(Player, through='TeamMembership')

    class Meta:
        verbose_name = "Squadra"
        verbose_name_plural = "Squadre"

    def __str__(self):
        return self.name


class TeamMembership(models.Model):
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    date_joined = models.DateField("Data", default=date.today)

    def __str__(self):
        return "Team " + self.team.name + " for event " + self.team.event.title
