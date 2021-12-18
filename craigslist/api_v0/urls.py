from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet
from .views import CategoryViewSet
from .views import AdvertisementViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
