from django.shortcuts import render
from .models import Movie, Category
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def top_chart(request, slug=None):
    categories = Category.objects.all()
    if slug:
        category = Category.objects.filter(slug=slug).first()
        movies = Movie.objects.filter(category=category).order_by("-rating")
    else:
        movies = Movie.objects.order_by('-rating')
    return render(request, 'main/chart.html', {'categories' : categories, 'movies' : movies})