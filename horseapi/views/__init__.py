# horseapi/views/__init__.py

from .auth import RegisterAPI, LoginAPI
from .horses import Horses
from .favorite_horses import FavoriteHorseViewSet
from .users import UserViewSet, LoginView
