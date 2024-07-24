from django.urls import include, path
from rest_framework import routers
from .views.horses import Horses
from .views.favorite_horses import FavoriteHorses
from .views.users import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'horses', Horses, basename='horse')
router.register(r'favorite_horses', FavoriteHorses, basename='favoritehorse')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
