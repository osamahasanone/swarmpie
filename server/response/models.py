from django.db import models


class ResponseParameterHeader(models.Model):
    key = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Response(models.Model):
    command = models.ForeignKey(
        'command.Command', on_delete=models.PROTECT, null=True)
    ts = models.DateTimeField(auto_created=True)


class ResponseParameter(models.Model):
    response = models.ForeignKey(
        'Response', on_delete=models.PROTECT, related_name='parameters')
    header = models.ForeignKey(
        'ResponseParameterHeader', on_delete=models.PROTECT)
    value = models.CharField(max_length=8000)
