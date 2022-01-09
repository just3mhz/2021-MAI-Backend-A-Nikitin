from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import index
from .views import advertisement
from .views import add_advertisement
from .views import login_view
from .views import search_view

urlpatterns = [
    path('', index, name="home"),
    path('advertisements/<int:advertisement_id>', advertisement),
    path('advertisements/add', add_advertisement),
    path('search/', search_view),
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
