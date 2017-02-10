from __future__ import unicode_literals
from django.apps import AppConfig


class AdidasConfig(AppConfig):
    name = 'adidas'

    def ready(self):
        from adidas import signals
        signals  # pyflakes
