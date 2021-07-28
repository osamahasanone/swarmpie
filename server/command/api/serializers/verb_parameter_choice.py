from rest_framework import serializers
from command.models import VerbParameterChoice


class VerbParameterChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbParameterChoice
        fields = ('id', 'header', 'value', 'description')
