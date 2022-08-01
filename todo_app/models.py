from re import M
from turtle import title
from venv import create
from django.db import models
from django.forms import CharField

class Todo(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created = models.DateTimeField()