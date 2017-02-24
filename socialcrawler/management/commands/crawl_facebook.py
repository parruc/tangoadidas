from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from socialcrawler.models import Post
import requests


class Command(BaseCommand):
    help = 'Crawls facebook for users posts'

    base_url = "https://graph.facebook.com/"
    tag_name = "#tangosquadmilano"

    def handle(self, *args, **options):
        output_partial = "Created {} posts and updated {} posts for user {}"
        output_final = "Created {} posts and updated {} posts  for {} users"
        app = SocialApp.objects.filter(provider="facebook").first()
        total_created = total_updated = users_count = 0
        for social_token in app.socialtoken_set.all():
            social_account = social_token.account
            user = social_account.user
            created = updated = 0
            params = {"token": social_token.token,
                      "uid": social_account.uid}
            uri = "{uid}/posts/?access_token={token}"
            url = self.base_url + uri.format(**params)
            r = requests.get(url)
            try:
                fb_posts = r.json().get("data", [])
            except ValueError:
                fb_posts = []
            for fb_post in fb_posts:
                if self.tag_name not in fb_post.get("message", ""):
                    continue
                post_id = fb_post["id"]
                params["id"] = post_id
                fb_reactions = {"likes": 0, "comments": 0, "sharedposts": 0}
                for fb_reaction in fb_reactions:
                    params["reaction"] = fb_reaction
                    uri = "{id}/{reaction}/?access_token={token}"
                    url = self.base_url + uri.format(**params)
                    r = requests.get(url)
                    try:
                        fb_reactions[fb_reaction] = len(r.json().get("data", []))
                    except ValueError:
                        fb_reactions[fb_reaction] = 0
                try:
                    post = Post.objects.get(provider="facebook",
                                            uid=post_id)
                    updated += 1
                except Post.DoesNotExist:
                    post = Post(uid=post_id, provider="facebook")
                    post.player = user
                    post.text = fb_post["message"]
                    created += 1
                post.likes = fb_reactions["likes"]
                post.comments = fb_reactions["comments"]
                post.shares = fb_reactions["sharedposts"]
                post.save()
            output = output_partial.format(created, updated, user.username)
            self.stdout.write(output)

            total_created += created
            total_updated += updated
            users_count += 1
        output = output_final.format(total_created, total_updated, users_count)
        self.stdout.write(output)
