# In models.py of your app

from django.db import models

class Study(models.Model):
    title = models.CharField(max_length=255)
    authors = models.TextField()
    abstract = models.TextField()
    citation = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
