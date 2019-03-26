from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Expenses(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=10,
                                 max_digits=10,
                                 validators=[MinValueValidator])
    currency = models.CharField(max_length=10)
    date = models.DateField(default=datetime.date.today)