from rest_framework import serializers
from response.models import ResponseParameter


class ResponseParameterSerializerResponse(serializers.ModelSerializer):

    class Meta:
        model = ResponseParameter
        fields = ('id', 'header', 'value')
        depth = 1
