from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Review, Director, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'opinion', 'movie']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'surname', 'age', 'movies']


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'year', 'director', 'full_name', 'director', 'category', 'reviews',
                  'actors']


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ['name', 'surname', 'age', 'movies']


class CategorySerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'movies']
