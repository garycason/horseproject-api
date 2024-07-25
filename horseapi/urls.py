from django.urls import path, include
from rest_framework.routers import DefaultRouter
from horseapi.views.horses import Horses
from horseapi.views.favorite_horses import FavoriteHorseViewSet
from horseapi.views.users import UserViewSet  # Assuming this exists

router = DefaultRouter()
router.register(r'horses', Horses, basename='horse')
router.register(r'favorite_horses', FavoriteHorseViewSet, basename='favoritehorse')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
