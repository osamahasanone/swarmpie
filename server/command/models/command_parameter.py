from django.db import models


class CommandParameter(models.Model):
    command = models.ForeignKey(
        'Command', on_delete=models.PROTECT, related_name='parameters')
    verb_parameter = models.ForeignKey(
        'VerbParameter', on_delete=models.PROTECT)
    value = models.CharField(max_length=8000)

    class Meta:
        unique_together = ('command', 'verb_parameter')

    def __str__(self):
        return self.value
