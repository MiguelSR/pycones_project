from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    python_level = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name
