from django.db import models
from datetime import datetime, date
from employee.models import Employee


class City(models.Model):
    name = models.CharField(max_length=124)

    def __str__(self):
        return self.name


class Directions(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Activities(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Treaties(models.Model):
    number = models.CharField(max_length=64, null=True)
    customer = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    term = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    type_of_work = models.CharField(max_length=512)
    cost = models.FloatField(max_length=64)
    cost_nds = models.FloatField(max_length=64)
    contacts = models.CharField(max_length=64)

    def __str__(self):
        return self.number


class Customers(models.Model):
    name = models.CharField(max_length=64)
    full_name = models.CharField(max_length=124)

    def __str__(self):
        return self.name


class TypesO(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class State(models.Model):

    name = models.CharField(max_length=64)
    number = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Doc(models.Model):
    date_start = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)    # дата начала
    adr = models.CharField(max_length=164)    # адрес
    Executor = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)    # Исполнитель
    activity = models.OneToOneField(Activities, on_delete=models.CASCADE, null=True)    # виды деятельности
    city = models.OneToOneField(City, on_delete=models.CASCADE, null=True)    # города
    country = models.OneToOneField(Country, on_delete=models.CASCADE, null=True)
    date_end = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)    # дата конца
    directions = models.OneToOneField(Directions, on_delete=models.CASCADE, null=True)    # направления деятельности
    treaties = models.OneToOneField(Treaties, on_delete=models.CASCADE, null=True)    # договоры
    customers = models.OneToOneField(Customers, on_delete=models.CASCADE, null=True)    # заказчики
    Types_objects = models.OneToOneField(TypesO, on_delete=models.CASCADE, null=True)    # виды объектов
    state_task = models.OneToOneField(State, on_delete=models.CASCADE, null=True)    # госзадание
