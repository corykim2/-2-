from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    complete = models.BooleanField(default=False)
