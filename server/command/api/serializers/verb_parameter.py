from rest_framework import serializers
from command.models import VerbParameter
from .verb_parameter_choice import VerbParameterChoiceSerializer


class VerbParameterSerializer(serializers.ModelSerializer):
    choices = VerbParameterChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = VerbParameter
        fields = ('id', 'order', 'choices')
