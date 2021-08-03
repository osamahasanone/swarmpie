from django.db import models


class Response(models.Model):
    command = models.ForeignKey(
        'command.Command', on_delete=models.PROTECT, null=True)
    ts = models.DateTimeField(auto_created=True)
