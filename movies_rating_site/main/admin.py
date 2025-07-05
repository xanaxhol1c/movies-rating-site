from django.contrib import admin
from .models import Category, Movie, UserRatings
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'imdb_rating', 'description', 'image', 'release_date']
    list_filter = ['name', 'category', 'imdb_rating']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(UserRatings)
class UserRatingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'score']
    list_filter = ['user', 'movie']