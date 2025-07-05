from django.db import models
from django.db.models import Avg
from .utils import upload_movie_image
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('main:chart_category', args=[self.slug])
    

class Movie(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True)
    imdb_rating = models.DecimalField(default=0.0, decimal_places=1, max_digits=3)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_movie_image, blank=True)
    release_date = models.DateField()

    class Meta:
        ordering = ['name', '-imdb_rating']
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
       return reverse('main:movie_details', args=[self.slug])

    def average_rating(self):
        ratings = UserRatings.objects.filter(movie=self).aggregate(avg=Avg('score'))

        rating = ratings['avg']
        if rating:
            return round(float(rating), 1)
        return None

class UserRatings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    review = models.TextField(max_length=250, blank=True, null=True)

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['user']
        verbose_name = "User Rating"
        verbose_name_plural = "User Ratings"

    def __str__(self):
        return str(f'{self.user.username} - {self.movie.name}: {self.score}')