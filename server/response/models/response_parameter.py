from django.db import models

class ResponseParameter(models.Model):
    response = models.ForeignKey(
        'Response', on_delete=models.PROTECT, related_name='parameters')
    header = models.ForeignKey(
        'ResponseParameterHeader', on_delete=models.PROTECT)
    value = models.CharField(max_length=8000)
