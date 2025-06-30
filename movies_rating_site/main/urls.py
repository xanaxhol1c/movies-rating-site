from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('chart/', views.top_chart, name='chart'),
]
