from rest_framework import serializers
from command.models import Command, CommandParameter
from . import CommandParameterSerializerResponse, CommandParameterSerializerRequest


class CommandSerializerResponse(serializers.ModelSerializer):
    parameters = CommandParameterSerializerResponse(many=True, read_only=True)

    class Meta:
        model = Command
        fields = ('id', 'verb', 'ts', 'parameters')
        depth = 1


class CommandSerializerRequest(serializers.ModelSerializer):
    parameters = CommandParameterSerializerRequest(many=True)

    class Meta:
        model = Command
        fields = ('id', 'verb', 'parameters')

    def create(self, validated_data):
        parameters_data = validated_data.pop('parameters')
        command = Command.objects.create(**validated_data)
        for parameter_data in parameters_data:
            CommandParameter.objects.create(command=command, **parameter_data)
        return command
