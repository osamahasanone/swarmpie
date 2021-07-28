from rest_framework import serializers
from command.models import CommandParameter


class CommandParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommandParameter
        fields = ('id', 'verb_parameter', 'value')
        depth = 1


class CommandParameterPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommandParameter
        fields = ('id', 'verb_parameter', 'value')
