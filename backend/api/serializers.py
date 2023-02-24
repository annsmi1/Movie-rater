from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Review, Director, Category, Actor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.opinion = validated_data.get('opinion', instance.opinion)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()

        return instance


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        depth = 1
        fields = ['id', 'title', 'description', 'year', 'director', 'full_name', 'director', 'category', 'reviews',
                  'actors']


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
