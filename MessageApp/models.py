from django.db import models

# Create your models here.

class Messages(models.Model):
    Id = models.AutoField(primary_key=True)
    Content = models.CharField(max_length=500)