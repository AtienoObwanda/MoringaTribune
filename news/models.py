from django.db import models

# Create your models here.

class Editor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.firstName

    class Meta:
        ordering = ['firstName']

class tags(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
        