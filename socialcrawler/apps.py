from django.apps import AppConfig
from django.core import management as django_management


def crawl_facebook(number):
    django_management.call_command('crawl_facebook')


def crawl_instagram(number):
    django_management.call_command('crawl_instagram')


class SocialCrawlerConfig(AppConfig):
    name = 'socialcrawler'
