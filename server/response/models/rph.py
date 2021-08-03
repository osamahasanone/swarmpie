from django.db import models


class ResponseParameterHeader(models.Model):
    key = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
