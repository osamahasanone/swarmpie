from django.db import models


class Command(models.Model):
    verb = models.ForeignKey('common.Verb', on_delete=models.PROTECT)
    ts = models.DateTimeField(auto_now_add=True)
