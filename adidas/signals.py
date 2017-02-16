"""
from adidas.models import Player
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User, dispatch_uid="adidas_user_creation")
def create_player_profile(sender, instance, created, **kwargs):
    if created:
        new_profile = Player.objects.create(user=instance)
        new_profile.save()
"""
