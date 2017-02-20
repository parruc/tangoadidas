"""
WSGI config for tangoadidas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from uwsgi import register_signal
from uwsgi import add_timer
from socialcrawler.apps import crawl_facebook
from socialcrawler.apps import crawl_instagram


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tangoadidas.settings")

application = get_wsgi_application()


register_signal(1, "worker", crawl_facebook)
add_timer(1, 30)
register_signal(2, "worker", crawl_instagram)
add_timer(2, 30)
