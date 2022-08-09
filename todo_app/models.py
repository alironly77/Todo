
from django.db import models


class Todo(models.Model):
    STATUS_CHOICES = (
        ("do", "Doing"),
        ("F", "Finish"),
        ("ns", "NotStarted")
    )
    Title = models.CharField(max_length=64)
    Description = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)
    Status_Choices = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default="ns")
