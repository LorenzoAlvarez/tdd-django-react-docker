from django.urls import path
from django.urls.resolvers import URLPattern

from .views import MovieDetail, MovieList

urlpatterns = [
    path("api/movies/", MovieList.as_view()),
    path("api/movies/<int:pk>/", MovieDetail.as_view())
]
