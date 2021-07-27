# Generated by Django 3.2.5 on 2021-07-26 16:43

from django.db import migrations


def insert_verb_parameter(apps, schema_editor):
    Verb = apps.get_model('common', 'Verb')
    VerbParameter = apps.get_model('command', 'VerbParameter')
    varb_paramter = ('TD', 1)
    verb = Verb.objects.filter(name=varb_paramter[0]).first()
    VerbParameter.objects.create(verb=verb, order=varb_paramter[1])


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0006_rename_verbparameterlegalstring_verbparameterchoice'),
    ]

    operations = [
        migrations.RunPython(insert_verb_parameter),
    ]