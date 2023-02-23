from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, MovieViewSet, ReviewViewSet, DirectorViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]