from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Post(models.Model):
    GENRE_CHOICES = {
        ('RO', 'Romance'),
        ('CO', 'Comedy'),
        ('RC', 'RomCom'),
        ('AN', 'Animation'),
        ('HO', 'Horror'),
        ('DR', 'Drama'),
        ('AC', 'Action'),
        ('SF', 'Science Fiction'),
        ('TJ', 'Tear Jerker'),
        ('FA', 'Fantasy'),
        ('CM', 'Classic Movie'),
        ('DM', 'Disaster Movie'),
        ('AM', 'Art Movie'),
        ('DO', 'Documentary'),
        ('MD', 'Mock Documentary'),
        ('BL', 'Blockbuster'),
        ('WH', 'Whodunnit'),
    }
    movie_title = models.CharField(max_length=64)
    movie_genre = models.CharField(max_length=2, choices=GENRE_CHOICES,null=True)
    running_time = models.IntegerField()
    review_content = models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=128)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    movie_created_at = models.IntegerField(validators=[MaxValueValidator(1700), MaxValueValidator(2100)])
    
