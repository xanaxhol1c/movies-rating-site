from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Category, UserRatings
from .forms import RateMovieForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-id')[:9]
    return render(request, 'main/index.html', {'movies' : movies})

def top_chart(request, slug=None):
    page = request.GET.get('page', 1)
    movies = None
    categories = Category.objects.all()
    if slug:
        category = Category.objects.filter(slug=slug).first()
        movies = Movie.objects.filter(category=category).order_by("-imdb_rating")
    else:
        movies = Movie.objects.order_by('-imdb_rating')
   
    if request.user.is_authenticated:
        user_ratings = UserRatings.objects.filter(user=request.user)
        ratings_map = {rating.movie.id: rating.score for rating in user_ratings}
        
        for movie in movies:
            rating = ratings_map.get(movie.id)
            movie.user_rating = rating

    paginator = Paginator(movies, 5)
    current_page = paginator.page(int(page))

    return render(request, 'main/chart.html', {'categories' : categories, 'current_page' : current_page})

@login_required
def movie_details(request, slug):
    movie = Movie.objects.filter(slug=slug).first()
    comments = UserRatings.objects.filter(movie=movie, review__isnull=False).exclude(review__exact='')

    try:
        rating = UserRatings.objects.get(user=request.user, movie=movie)
    except UserRatings.DoesNotExist:
        rating = None

    if request.method == 'POST':
        form = RateMovieForm(request.POST, instance=rating)

        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.user = request.user
            new_rating.movie = movie
            new_rating.save()
            return redirect('main:movie_details', slug = movie.slug)
    else:
        form = RateMovieForm(instance=rating)

    return render(request, 'main/moviedetails.html', {'form' : form, 'movie' : movie, 'rating' : rating, 'comments' : comments})

def search_movie(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    page = request.GET.get('page', 1)
    movies = Movie.objects.filter(name__iregex=q)
    categories = Category.objects.all()

    if movies:
        paginator = Paginator(movies, 5)
        current_page = paginator.page(int(page))
        return render(request, 'main/chart.html', {'categories' : categories, 'current_page' : current_page})

    messages.error(request, message=f'Sorry, but movie with name "{q}" is not found.')
    return render(request, 'main/chart.html')

# def rate_movie(request, slug):
#     movie = get_object_or_404(Movie, slug=slug)
#     rating, created = UserRatings.objects.update_or_create(user=request.user, movie=movie)

#     if request.method == 'POST':
#         form = RateMovieForm(request.POST, instance=rating)

#         if form.is_valid():
#             form.save()
#             return redirect('main:movie_details', slug = movie.slug)
#     else:
#         form = RateMovieForm(instance=rating)

#     return render(request, 'main/moviedetails.html', {'form' : form, 'movie' : movie})
