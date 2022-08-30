from django.contrib import admin
from posts.models import Post, Comment, Keyword

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Keyword)
