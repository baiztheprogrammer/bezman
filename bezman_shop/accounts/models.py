from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    phone = models.IntegerField()

    def __str__(self):
        return self.full_name


