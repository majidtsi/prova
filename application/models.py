from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Cliente(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reservation = models.ForeignKey('Reservation',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.user.username
class Piatti(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    ordini = models.ForeignKey('Ordini', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return str(self.date)

class Ordini(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)
    prenota = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.cliente.user.username

def create_cliente(sender,**kwargs):
    print(kwargs)
    if kwargs["created"]:
        user_profile = Cliente.objects.create(user=kwargs['instance'])

post_save.connect(create_cliente,sender=User)