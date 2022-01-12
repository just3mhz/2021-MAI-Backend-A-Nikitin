from django.urls import path

from .views import connect
from .views import publish
from .views import subscribe

urlpatterns = [
    path('connect/', connect, name='connect'),
    path('subscribe/', subscribe, name='subscribe'),
    path('publish/', publish, name='publish'),
]
