from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPI, LoginAPI, FavoriteHorseViewSet, UserViewSet, LoginView, Horses

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'favoritehorses', FavoriteHorseViewSet, basename='favoritehorse')
router.register(r'horses', Horses, basename='horse')

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('api-token-auth/', LoginView.as_view(), name='api_token_auth'),
    path('', include(router.urls)),
]
