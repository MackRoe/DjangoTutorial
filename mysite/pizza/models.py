from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=200)


class Pizza(models.Model):
    pizza = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateTimeField('date ordered')
    toppings = models.ManyToManyField(Topping)
