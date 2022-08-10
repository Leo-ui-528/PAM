from django.db import models
from datetime import datetime, date


class Owner(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Employee(models.Model):

    employee = models.CharField(max_length=64)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.employee
