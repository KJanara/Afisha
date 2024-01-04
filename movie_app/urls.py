from django.urls import path
from . import views
urlpatterns = [
  path('directors/', views.director_list),
  path('directors/<int:id>/', views.director_detail),
  path('movies/', views.movies_list),
  path('movies/<int:id>/', views.movies_detail),
  path('reviews/', views.review_list),
  path('reviews/<int:id>/', views.review_detail),
  path('movies/reviews/', views.movie_reviews),
]
