from .models import Post
from django.contrib import admin


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">chat_bubble_outline</i>'
