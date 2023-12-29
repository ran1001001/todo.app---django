from django.db import models

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=32)
    description = models.TextField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.todo}: {self.status}"
