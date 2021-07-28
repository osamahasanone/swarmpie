from rest_framework import serializers
from command.models import Command, CommandParameter
from . import CommandParameterSerializer, CommandParameterPostSerializer


class CommandSerializer(serializers.ModelSerializer):
    parameters = CommandParameterSerializer(many=True, read_only=True)

    class Meta:
        model = Command
        fields = ('id', 'verb', 'ts', 'parameters')
        depth = 1


class CommandPostSerializer(serializers.ModelSerializer):
    parameters = CommandParameterPostSerializer(many=True)

    class Meta:
        model = Command
        fields = ('id', 'verb', 'parameters')

    def create(self, validated_data):
        parameters_data = validated_data.pop('parameters')
        command = Command.objects.create(**validated_data)
        for parameter_data in parameters_data:
            CommandParameter.objects.create(command=command, **parameter_data)
        return command
