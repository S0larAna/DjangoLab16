from django.db import models
from django import forms

class Client(models.Model):
    firstname = models.CharField(max_length=200)
    secondname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)
    checking_account = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.firstname

    @property
    def item_count(self):
        return str(Jewelry.objects.filter(client=self).count())

class Store(models.Model):
    address = models.CharField(max_length=500)
    opened = models.BooleanField()

    @property
    def item_count(self):
        return str(Jewelry.objects.filter(store=self).count())

class Jewelry(models.Model):
    TYPE = (
        ('Ring', 'Ring'),
        ('Brooch', 'Brooch'),
        ('Bracelet', 'Bracelet'),
        ('Anklet', 'Anklet'),
        ('Necklace', 'Necklace'),
        ('Earring', 'Earring'),
        ('Cuff links', 'Cuff links'),
        ('Locket', 'Locket'),
        ('Pendant', 'Pendant')
    )
    type = models.CharField(max_length=200, choices=TYPE)
    material = models.CharField(max_length=200)
    defects = models.CharField(max_length=500)
    date = models.DateField()
    price = models.FloatField()
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.type


class User(models.Model):
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    secondname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=200)


