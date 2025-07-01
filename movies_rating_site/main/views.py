from django.shortcuts import render
from .models import Movie, Category
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def top_chart(request, slug=None):
    categories = Category.objects.all()
    if slug:
        category = Category.objects.filter(slug=slug).first()
        movies = Movie.objects.filter(category=category).order_by("-imdb_rating")
    else:
        movies = Movie.objects.order_by('-imdb_rating')
    return render(request, 'main/chart.html', {'categories' : categories, 'movies' : movies})

def movie_details(request, slug):
    movie = Movie.objects.filter(slug=slug).first()
    return render(request, 'main/moviedetails.html', {'movie' : movie})