from django.db import models
# test comment
# Create your models here.


class Comment(models.Model):
    date = models.DateField('%m/%d/%Y', null=True, blank=True)
    like_count = models.IntegerField(default=0)
    video_id = models.CharField(max_length=20, null=True, blank=True)
    content = models.CharField(max_length=250, null=True, blank=True)
    replies = models.CharField(max_length=50, null=True, blank=True)
