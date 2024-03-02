from django.contrib import admin
from .models import Post, Media, Story, Mention

admin.site.register(Post)
admin.site.register(Media)
admin.site.register(Story)
admin.site.register(Mention)
