from django.db import models
from django.contrib.auth.models import User
from .horse import Horse

class FavoriteHorse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_horses')
    horse = models.ForeignKey(Horse,on_delete=models.CASCADE,related_name="favorited_by")