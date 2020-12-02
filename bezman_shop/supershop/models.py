from django.db import models

# Create your models here.


class Product(models.Model):
    types = (
        ('Classic','Classic'),
        ('Sport','Sport'),
        ('dm','demi-season'),
        ('Winter','Winter'),
    )
    genders = (
        ('Male','Male'),
        ('Female','Female'),
        ('Uni','Uni')
    )

    sizes = (
    ('Child','Child'),
    ('Medium','Medium'),
    ('Large','Large'),
    ('XL','XL'),
    )
    name = models.CharField(max_length=40)
    product_type = models.CharField(max_length=40,choices=types)
    gender = models.CharField(max_length=20,choices=genders)
    product_model = models.CharField(max_length=50)
    price = models.IntegerField()
    size = models.CharField(max_length=20,choices=sizes)
    image = models.ImageField(blank=True,default='default.png')
    manufacturer = models.CharField(max_length=15)



    def __str__(self):
        return self.name+' '+self.product_model


class Order(models.Model):
    statuses = (
        ('Not Delivered','Not Delivered'),
        ('In Process','In Process'),
        ('Delivered','Delivered')
    )
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=statuses,default='Not Delivered')

    def __str__(self):
        return self.product.name + ' ' + self.status
