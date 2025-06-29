from django.contrib import admin
from .models import Category, Movie
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'rating', 'description', 'image', 'release_date']
    list_filter = ['name', 'category', 'rating']
    prepopulated_fields = {'slug' : ('name',)}
