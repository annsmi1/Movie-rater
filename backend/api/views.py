from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Movie
from .serializers import MovieSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

