from django.db import models


class VerbParameterChoice(models.Model):
    verb_parameter = models.ForeignKey(
        'VerbParameter', on_delete=models.PROTECT, related_name='choices')
    header = models.CharField(max_length=10)
    value = models.CharField(max_length=8000)
    description = models.TextField()

    class Meta:
        unique_together = ('verb_parameter', 'header', 'value')

    def __str__(self):
        if self.header:
            return f'{self.header}={self.value}'
        return self.value
