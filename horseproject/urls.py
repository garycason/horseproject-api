from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from horseapi.views.users import LoginView

urlpatterns = [
    path('api/', include('horseapi.urls')),  # Ensure 'api/' is included in the path
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', LoginView.as_view(), name='login'),  # Directly add the LoginView here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
