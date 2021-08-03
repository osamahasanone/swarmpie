from rest_framework import serializers
from command.models import VerbParameter
from . import VerbParameterChoiceSerializerResponse


class VerbParameterSerializerResponse(serializers.ModelSerializer):
    choices = VerbParameterChoiceSerializerResponse(many=True, read_only=True)

    class Meta:
        model = VerbParameter
        fields = ('id', 'order', 'choices')
