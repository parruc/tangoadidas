from django.db import models
from adidas.models import Player

# Create your models here.


PROVIDER_CHOICES = (
    (u'facebook', u'Facebook'),
    (u'instagram', u'Instagram'),
)


class Post(models.Model):
    uid = models.CharField("UID", max_length=100)
    provider = models.CharField("Provider", max_length=19,
                                choices=PROVIDER_CHOICES)
    text = models.TextField("Testo", default="")
    image_url = models.TextField("Url Immagine", default="")
    player = models.ForeignKey(Player)
    likes = models.IntegerField("Likes", default=0)
    comments = models.IntegerField("Commenti", default=0)
    shares = models.IntegerField("Condivisioni", default=0)

    class Meta():
        unique_together = ('uid', 'provider',)

    @property
    def points(self):
        """ 1 point for each Post
            2 points for each Likes
            2 point for each comment
            5 poinst for each share (FB only)
        """
        return self.likes * 2 + self.comments * 2 + self.shares * 5 + 1
