from django.contrib import admin
from django.urls import path, include
from horseapi.views.auth import RegisterAPI, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('horseapi.urls')),
    path('api/auth/register/', RegisterAPI.as_view(), name='register'),
    path('api/auth/login/', LoginAPI.as_view(), name='login'),
]
