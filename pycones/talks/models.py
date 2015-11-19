from django.db import models

from authors.models import Author

# Create your models here.

class Talk(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    authors = models.ManyToManyField(Author, related_name='talks') 

    def __unicode__(self):
        return self.name
