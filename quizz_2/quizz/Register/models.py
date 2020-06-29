from django.db import models


class RegisterList(models.Model):
    name = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    mobnum = models.CharField(max_length=250)
