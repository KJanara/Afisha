from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
    def get_movies_count(self, obj):
      return obj.movie_set.count()

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 2

class DirectorValidateSerializer(serializers.Serializer):
  name = serializers.CharField()

class MovieValidateSerializer(serializers.Serializer):
  title = serializers.CharField()
  description= serializers.CharField()
  duration = serializers.IntegerField()
  director_id = serializers.IntegerField()

  def validate_director_id(self, director_id):
    try:
      Director.objects.get(id=director_id)
    except Director.DoesNotExist:
      raise ValidationError('Director does not exist')
    return director_id



class ReviewValidateSerializer(serializers.Serializer):
  text = serializers.CharField()
  stars = serializers.IntegerField()
  movie_id = serializers.IntegerField()

  def validate_movie_id(self, movie_id):
    try:
      Director.objects.get(id=movie_id)
    except Director.DoesNotExist:
      raise ValidationError('movie does not exist')
    return movie_id
