from django.db import models

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.todo}: {self.status}"
