# Generated by Django 3.2.5 on 2021-08-02 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0007_alter_responseparameterheader_key'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResponseParameterHeaderVerb',
        ),
    ]
