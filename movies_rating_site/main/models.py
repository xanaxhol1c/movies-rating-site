from django.db import models
from .utils import upload_movie_image
from django.urls import reverse
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
        return reverse('main:chart', args=[self.slug])
    

class Movie(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True)
    rating = models.DecimalField(default=0.00, decimal_places=2, max_digits=3)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_movie_image, blank=True)
    release_date = models.DateField()

    class Meta:
        ordering = ['name', '-rating']
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return str(self.name)