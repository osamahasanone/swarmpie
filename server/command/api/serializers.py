from rest_framework import serializers
from command.models import *


class VerbParameterChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbParameterChoice
        fields = ('id', 'header', 'value', 'description')


class VerbParameterSerializer(serializers.ModelSerializer):
    choices = VerbParameterChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = VerbParameter
        fields = ('id', 'order', 'choices')


class CommandParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommandParameter
        fields = ('id', 'verb_parameter', 'value')
        depth = 1


class CommandSerializer(serializers.ModelSerializer):
    verb = serializers.SerializerMethodField()
    parameters = CommandParameterSerializer(many=True, read_only=True)

    class Meta:
        model = Command
        fields = ('id', 'verb', 'ts', 'parameters')

    def get_verb(self, command):
        return command.verb.name
