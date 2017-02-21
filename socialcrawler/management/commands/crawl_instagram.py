from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from socialcrawler.models import Post
import requests


class Command(BaseCommand):
    help = 'Crawls facebook for users posts'

    base_url = "https://api.instagram.com/v1/"
    tag_name = "tangosquadmilano"

    def handle(self, *args, **options):
        output_partial = "Created {} posts and updated {} posts for user {}"
        output_final = "Created {} posts and updated {} posts  for {} users"
        app = SocialApp.objects.filter(provider="instagram").first()
        total_created = total_updated = users_count = 0
        for social_token in app.socialtoken_set.all():
            social_account = social_token.account
            user = social_account.user
            created = updated = 0
            params = {"token": social_token.token,
                      "uid": social_account.uid}
            uri = "users/{uid}/media/recent/?access_token={token}"
            url = self.base_url + uri.format(**params)
            r = requests.get(url)
            try:
                instagram_posts = r.json().get("data", [])
            except ValueError:
                instagram_posts = []
            for instagram_post in instagram_posts:
                if self.tag_name not in instagram_post["tags"]:
                    continue
                post_id = instagram_post["id"]
                try:
                    post = Post.objects.get(provider="instagram",
                                            uid=post_id)
                    updated += 1
                except Post.DoesNotExist:
                    images = instagram_post["images"]
                    post = Post(uid=post_id, provider="instagram")
                    post.player = user
                    post.text = instagram_post["caption"]["text"]
                    post.image_url = images["standard_resolution"]["url"]
                    created += 1
                post.likes = instagram_post["likes"]["count"]
                post.comments = instagram_post["comments"]["count"]
                post.save()
            output = output_partial.format(created, updated, user.username)
            self.stdout.write(output)

            total_created += created
            total_updated += updated
            users_count += 1
        output = output_final.format(total_created, total_updated, users_count)
        self.stdout.write(output)
