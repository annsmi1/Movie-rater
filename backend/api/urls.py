from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, MovieViewSet, ReviewViewSet, DirectorViewSet, CategoryViewSet,ActorViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'reviews', ReviewViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'actors', ActorViewSet, basename='actors')

urlpatterns = [
    path('', include(router.urls)),
]