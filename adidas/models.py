from __future__ import unicode_literals
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.username, filename)


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


class Player(AbstractUser):
    is_leader = models.BooleanField(default=False)
    points = models.ManyToManyField(Event, through='PlayerPoints')
    image = models.ImageField(upload_to=user_directory_path, null=True, )

    class Meta:
        verbose_name = "Giocatore"
        verbose_name_plural = "Giocatori"
        db_table = 'auth_user'

    @property
    def stars(self):
        points = self.get_points()
        thresholds = [100, 200, 400, 800, 2000]
        stars = 0
        for threshold in thresholds:
            if points > threshold:
                stars += 1
        return stars

    def get_points(self):
        points = 0
        for post in self.post_set.all():
            points += post.points
        return points


class PlayerPoints(models.Model):
    player = models.ForeignKey(Player)
    event = models.ForeignKey(Event)
    points = models.IntegerField("Punti")

    def __str__(self):
        return "Team " + self.team.name + " for event " + self.team.event.title


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
