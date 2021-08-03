from rest_framework import serializers
from response.models import Response, ResponseParameter
from . import ResponseParameterSerializerResponse


class ResponseSerializerResponse(serializers.ModelSerializer):
    parameters = ResponseParameterSerializerResponse(many=True, read_only=True)

    class Meta:
        model = Response
        fields = ('id', 'command', 'ts', 'parameters')
        depth = 2
