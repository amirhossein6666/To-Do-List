from django.db import models
from django.contrib.auth.models import User

class Todo (models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)

    def __str__(self) :
        return self.title