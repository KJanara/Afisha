from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer,
                          MovieValidateSerializer, DirectorValidateSerializer, ReviewValidateSerializer)


@api_view(['GET', 'POST'])
def director_list(request):
    if request.method == 'GET':
      directors = Director.objects.all()
      serializer = DirectorSerializer(directors, many=True)
      return Response(serializer.data)
    elif request.method == 'POST':
      serializer = DirectorValidateSerializer(data=request.data)
      if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
      name = serializer.validated_data.get('name')
      director = Director.objects.create(name=name)
      return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
  try:
    director = Director.objects.get(id=id)
  except:
    return Response(data={'massage': 'movie nit found'}, status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = DirectorSerializer(director, many=False)
    return Response(serializer.data)
  elif request.method == 'PUT':
    director.name = request.data.get('name')
    return Response(data=MovieSerializer(director).data)
  elif request.method == 'DELETE':
    director.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def movies_list(request):
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = MovieValidateSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
    title = serializer.validated_data.get('title')
    description =serializer.validated_data.get('description')
    duration = serializer.validated_data.get('duration')
    director_id = serializer.validated_data.get('director_id')
    movie = Movie.objects.create(title=title, description=description,
                                 duration=duration, director_id=director_id)
    return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail(request, id):
  try:
    movie = Movie.objects.get(id=id)
  except Movie.DoesNotExist:
    return Response(data={'massage': 'movie nit found'}, status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = MovieSerializer(movie, many=False)
    return Response(data=serializer.data)
  elif request.method == 'PUT':
    movie.title = request.data.get('title')
    movie.description = request.data.get('description')
    movie.duration = request.data.get('duration')
    movie.director_id = request.data.get('director_id')
    return Response(data=MovieSerializer(movie).data)
  elif request.method == 'DELETE':
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def review_list(request):
  if request.method == 'GET':
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ReviewValidateSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
    text = serializer.validated_data.get('text')
    stars =serializer.validated_data.get('stars')
    movie_id =serializer.validated_data.get('movie_id')
    review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
    return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
  try:
    review = Director.objects.get(id=id)
  except:
    return Response(data={'massage': 'movie nit found'}, status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = DirectorSerializer(review, many=False)
    return Response(serializer.data)
  elif request.method == 'PUT':
    review.text = request.data.get('text')
    review.stars = request.data.get('stars')
    review.movie_id = request.data.get('movie_id')
    return Response(data=MovieSerializer(review).data)
  elif request.method == 'DELETE':
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

