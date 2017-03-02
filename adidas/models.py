from __future__ import unicode_literals
from datetime import date
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from uuid import uuid1


def generate_uid():
    return uuid1().hex


def valid_birth_date(value):
    min_date = value + timedelta(days=16*365.25)
    max_date = value + timedelta(days=25*365.25)
    if date.today() < min_date or date.today() > max_date:
        raise ValidationError('La tua età deve essere tra 16 e 25 anni',
                              code='birth_date')


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.username, filename)


def event_directory_path(instance, filename):
    return 'event_{0}/{1}'.format(slugify(instance.title), filename)


class Event(models.Model):
    title = models.CharField("Titolo", max_length=128)
    description = models.TextField("Descrizione", null=True)
    place = models.CharField("Luogo", max_length=256, null=True)
    image = models.ImageField("Immagine del'evento",
                              upload_to=event_directory_path, null=True, )
    start_date = models.DateField("Data di inizio", default=date.today)
    start_time = models.TimeField("Ora di inizio", default=datetime.now)
    end_date = models.DateField("Data di fine", default=date.today)
    end_time = models.TimeField("Ora di fine", default=datetime.now)
    allowed_teams = models.ManyToManyField('Team',
                                           related_name="allowed_teams",
                                           verbose_name="Squadre abilitate", )
    teams = models.ManyToManyField('Team', blank=True, null=True,
                                   verbose_name="Squadre iscritte")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"

    def __str__(self):
        return self.title


class Player(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\d{7,13}$',
                                 message="Numero di telefono non valido.")
    is_leader = models.BooleanField(default=False)
    birth_date = models.DateField('Data di nascita', default=date.today,
                                  validators=[valid_birth_date, ])
    points_in_event = models.ManyToManyField('Event', verbose_name="Punti",
                                             through='PlayerPointsInEvent')
    image = models.ImageField("Immagine del profili",
                              upload_to=user_directory_path, null=True, )
    phone_number = models.CharField(validators=[phone_regex], max_length=13,
                                    verbose_name="Numero di telefono",
                                    null=True)
    team = models.ForeignKey('Team', null=True)
    date_joined = models.DateField("Data", default=date.today)

    class Meta:
        verbose_name = "Giocatore"
        verbose_name_plural = "Giocatori"
        db_table = 'auth_user'

    @property
    def stars(self):
        points = self.get_social_points()
        thresholds = [60, 180, 400, 800, 1000]
        stars = 0
        for threshold in thresholds:
            if points > threshold:
                stars += 1
        return stars

    @property
    def events_points(self):
        points = 0
        for point in self.points_in_event:
            points += point
        return points

    def get_social_points(self):
        points = 0
        for post in self.post_set.all():
            points += post.points
        return points


class PlayerPointsInEvent(models.Model):
    player = models.ForeignKey('Player', verbose_name="Giocatore")
    event = models.ForeignKey('Event', verbose_name="Evento")
    points = models.IntegerField(verbose_name="Punti")

    def __str__(self):
        return "Player {} for event {}".format(self.player.username,
                                               self.event.title)


class Team(models.Model):
    name = models.CharField("Nome", max_length=128)
    hash = models.CharField("Codice adesione", max_length=50,
                            default=generate_uid)

    class Meta:
        verbose_name = "Squadra"
        verbose_name_plural = "Squadre"

    def __str__(self):
        return self.name
