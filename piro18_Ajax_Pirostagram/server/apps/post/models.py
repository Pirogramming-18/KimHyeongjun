from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.BooleanField(default=False)

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post")