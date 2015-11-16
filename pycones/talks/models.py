from django.db import models

from authors.models import Author

# Create your models here.

class Talk(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=2048, null=False, blank=False)
    authors = models.ManyToManyField(Author) 
