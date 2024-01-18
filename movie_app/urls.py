from django.urls import path
from . import views
urlpatterns = [
  # path('directors/', views.director_list),
  # path('directors/<int:id>/', views.director_detail),
  # path('movies/', views.movies_list),
  # path('movies/<int:id>/', views.movies_detail),
  # path('reviews/', views.review_list),
  # path('reviews/<int:id>/', views.review_detail),

  path('director/', views.DirectorListAPIView.as_view()),
  path('director/<int:id>/', views.DirectorDetailAPIView.as_view()),
  path('movies/', views.MovieListAPIView.as_view()),
  path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
  path('reviews/', views.ReviewListAPIView.as_view()),
  path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
]

