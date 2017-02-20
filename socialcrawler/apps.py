from django.apps import AppConfig
from django.core import management

import uwsgi


def crawl_facebook():
    management.call_command('crawl_facebook')


def crawl_instagram():
    management.call_command('crawl_facebook')


class SocialCrawlerConfig(AppConfig):
    name = 'socialcrawler'
    def ready(self):
        import uwsgi
        uwsgi.register_signal(1, "worker", crawl_facebook)
        uwsgi.add_timer(1, 30)
        uwsgi.register_signal(2, "worker", crawl_instagram)
        uwsgi.add_timer(2, 30)
