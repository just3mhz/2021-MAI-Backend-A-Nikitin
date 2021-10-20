from django.urls import path

from .views import by_category
from .views import advertisement
from .views import add_advertisement
from .views import user

urlpatterns = [
    path('category/<int:category>', by_category),
    path('advertisement/<int:ad_id>', advertisement),
    path('add/advertisement', add_advertisement),
    path('user/<int:user_id>', user)
]
