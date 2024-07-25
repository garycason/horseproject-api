from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from horseapi.views import register_user, login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('horseapi.urls')),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
]

