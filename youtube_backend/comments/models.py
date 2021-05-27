from django.db import models
# test comment
# Create your models here.


class Comment(models.Model):
    date = models.DateField('%m/%d/%Y')
    like_count = models.IntegerField(default=0)
    video_id = ''
    content = []
    replies = []
