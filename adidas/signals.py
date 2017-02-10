from adidas.models import Player
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_player_profile(sender, instance, created, **kwargs):
    if created:
        new_profile = Player.objects.create(user=instance)
        new_profile.save()


post_save.connect(create_player_profile, sender=User)
