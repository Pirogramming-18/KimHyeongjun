from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class DevTool(models.Model):
    name = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    content =  models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    interest = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE)