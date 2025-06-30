from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def top_chart(request):
    movies = Movie.objects.all()
    return render(request, 'main/chart.html', {'movies' : movies})