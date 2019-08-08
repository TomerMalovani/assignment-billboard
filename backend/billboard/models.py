from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post_content = models.CharField(max_length=200)
    post_author = models.CharField(max_length=10)
