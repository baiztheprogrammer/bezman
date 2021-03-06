from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    phone = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.full_name




