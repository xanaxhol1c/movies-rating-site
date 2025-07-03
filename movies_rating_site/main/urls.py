from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('chart/', views.top_chart, name='chart'),
    path('chart/search/', views.search_movie, name='search_movie'),
    path('chart/category/<slug:slug>/', views.top_chart, name='chart_category'),
    path('chart/<slug:slug>/', views.movie_details, name='movie_details'),
    # path('chart/<slug:slug>/rate/', views.rate_movie, name='rate_movie'),
]
