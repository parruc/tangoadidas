from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(verbose_name="Titolo", max_length=128)
    date = models.DateField(verbose_name="Data")
    time = models.TimeField(verbose_name="Data")
    place = models.TextField(verbose_name="Luogo")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=128)
    event = models.ForeignKey(Event)
    members = models.ManyToManyField(User, through='TeamMembership')

    class Meta:
        verbose_name = "Squadra"
        verbose_name_plural = "Squadre"

    def __str__(self):
        return self.name


class TeamMembership(models.Model):
    player = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    date_joined = models.DateField()
    leader = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return "Team " + team.name + " enrolled for event " + event.title
