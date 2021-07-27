from rest_framework import serializers
from command.models import *


class VerbParameterChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbParameterChoice
        fields = ('id', 'header', 'value', 'description')


class VerbParameterSerializer(serializers.ModelSerializer):
    choices = VerbParameterChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = VerbParameter
        fields = ('id', 'order', 'choices')
