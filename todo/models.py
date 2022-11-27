from statistics import mode
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    created = models.DateTimeField()
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)


    def __str__(self):
        return self.title
