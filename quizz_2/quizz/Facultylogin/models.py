from django.db import models


class FacultyList(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=100)


class Subjects(models.Model):
    department = models.CharField(max_length=250)


class CSE(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


class ECE(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


class EEE(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


class APTITUDE(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


class GK(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)

