from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class VerbParameter(models.Model):
    verb = models.ForeignKey('common.Verb', on_delete=models.PROTECT)
    order = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2)])

    class Meta:
        unique_together = ('verb', 'order')


