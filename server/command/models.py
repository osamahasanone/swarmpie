from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class VerbParameter(models.Model):
    verb = models.ForeignKey(
        'common.Verb', on_delete=models.PROTECT, related_name='parameters')
    order = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2)])

    class Meta:
        unique_together = ('verb', 'order')

    def __str__(self):
        return f'{self.verb} param #{self.order}'


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


class Command(models.Model):
    verb = models.ForeignKey('common.Verb', on_delete=models.PROTECT)
    ts = models.DateTimeField(auto_created=True)


class CommandParameter(models.Model):
    command = models.ForeignKey('Command', on_delete=models.PROTECT)
    verb_parameter = models.ForeignKey(
        'VerbParameter', on_delete=models.PROTECT)
    value = models.CharField(max_length=8000)

    class Meta:
        unique_together = ('command', 'verb_parameter')

    def __str__(self):
        return self.value
