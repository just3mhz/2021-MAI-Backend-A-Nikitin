from django.urls import path

from .views import index
from .views import advertisement
from .views import add_advertisement

urlpatterns = [
    path('', index),
    path('advertisements/<int:advertisement_id>', advertisement),
    path('advertisements/add', add_advertisement),
]
