from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Post(models.Model):
    movie_title = models.CharField(max_length=64)
    movie_genre = models.CharField(max_length=32)
    running_time = models.IntegerField()
    review_content = models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=128)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    movie_created_at = models.IntegerField(validators=[MaxValueValidator(1700), MaxValueValidator(2100)])
    
