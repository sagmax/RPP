from django.db import models
from django.contrib import admin
import datetime
from django.utils import timezone
from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cashier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Check(models.Model):
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    total_sum = models.DecimalField(max_digits=999999, decimal_places=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f'Отчет №{self.pk}'


class Sale(models.Model):
    check_id = models.ForeignKey(Check, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Sale #{self.pk}'
