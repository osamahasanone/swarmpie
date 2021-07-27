from rest_framework import serializers
from common.models import *
from command.api.serializers import VerbParameterSerializer


class VerbSerializer(serializers.ModelSerializer):
    parameters = VerbParameterSerializer(many=True, read_only=True)

    class Meta:
        model = Verb
        fields = ('id', 'name', 'description', 'parameters')
        depth = 2
