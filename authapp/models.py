from django.db import models
from datetime import datetime
from django.contrib.auth.models import User  
# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length = 150)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()
    created_at=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name