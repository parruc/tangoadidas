from django.apps import AppConfig

import uwsgi


def crawl_socials(num):
    print("crawling socials")


class SocialcrawlerConfig(AppConfig):
    name = 'socialcrawler'

    def ready(self):
        uwsgi.register_signal(26, "worker", crawl_socials)
        uwsgi.add_timer(26, 3600)
