from rest_framework import serializers
from common.models import Verb
from command.serializers import VerbParameterSerializerResponse


class VerbSerializerResponse(serializers.ModelSerializer):
    parameters = VerbParameterSerializerResponse(many=True, read_only=True)

    class Meta:
        model = Verb
        fields = ('id', 'name', 'description', 'parameters')
        depth = 2
