from django.contrib.auth.models import User
from django.db import models

class Horse(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    total_races = models.IntegerField()
    total_earnings = models.DecimalField(max_digits=10,decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='horses')
    