from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('api/v0/', include('api_v0.urls')),
    path('social_auth/', include('social_django.urls', namespace='social')),
]
