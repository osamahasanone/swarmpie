from django.db import models


class ResponseParameterHeader(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(null=True, max_length=1000)

    def __str__(self):
        return self.name


class ResponseParameterHeaderVerb(models.Model):
    verb = models.ForeignKey(
        'common.Verb', on_delete=models.PROTECT, related_name='response_headers')
    header = models.ForeignKey(
        'ResponseParameterHeader', on_delete=models.PROTECT, related_name='verbs')


class Response(models.Model):
    verb = models.ForeignKey('common.Verb', on_delete=models.PROTECT)
    ts = models.DateTimeField(auto_created=True)


class ResponseParameter(models.Model):
    response = models.ForeignKey(
        'Response', on_delete=models.PROTECT, related_name='parameters')
    header = models.ForeignKey(
        'ResponseParameterHeader', on_delete=models.PROTECT)
    value = models.CharField(max_length=8000)
