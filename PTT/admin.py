from django.contrib import admin
from .models import Topic, Sort, Post, Option, Comment

admin.site.register(Topic)
admin.site.register(Sort)
admin.site.register(Post)
admin.site.register(Option)
admin.site.register(Comment)

