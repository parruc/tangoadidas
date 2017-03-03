from adidas.models import Player
from adidas.models import Team
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Player, dispatch_uid="adidas_player_creation")
def assign_is_capitain(sender, instance, created, **kwargs):
    if created:
        if not instance.is_captain:
            if instance.email in getattr(settings, "CAPTAIN_EMAILS", []):
                team = Team()
                team.save()
                instance.team = team
                instance.is_captain = True
                instance.save()
