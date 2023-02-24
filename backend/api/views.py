from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import UserSerializer
from .models import Movie, Review, Director, Category, Actor
from .serializers import MovieSerializer, ReviewSerializer, DirectorSerializer, CategorySerializer, ActorSerializer


class SetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    #filter_fields = ('title', 'year', 'director')
    search_fields = ('title', 'year', 'description', 'category__name')
    ordering_fields = '__all__'
    ordering = ('year',)
    pagination_class = SetPagination

    def get_queryset(self):
        movies = Movie.objects.all()
        return movies


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ActorViewSet(viewsets.ModelViewSet):

    serializer_class = ActorSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'surname')
    ordering_fields = '__all__'
    ordering = ('surname',)
    pagination_class = SetPagination

    def get_queryset(self):
        actors = Actor.objects.all()
        return actors

    @action(detail=True, methods=['post'])
    def add_movie(self, request, **kwargs):
        actor = self.get_object()
        movie = Movie.objects.get(id=request.data['movie'])
        actor.movies.add(movie)

        serializer = ActorSerializer(actor, many = False)
        return Response(serializer.data)



