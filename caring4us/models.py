# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200, primary_key = True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    carer = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Illness(models.Model):
    illness = models.CharField(max_length=200, primary_key = True)
    severity = models.CharField(max_length=200)
    medication = models.BooleanField()

class Carers(models.Model):
    name = models.CharField(max_length=200, primary_key = True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    give_car_to = models.ForeignKey(Person)
