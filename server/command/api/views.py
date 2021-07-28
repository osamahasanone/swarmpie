from command.models import VerbParameter, CommandParameter, Command
from .serializers import *
from rest_framework import generics


class VerbParameterList(generics.ListAPIView):
    queryset = VerbParameter.objects.all()
    serializer_class = VerbParameterChoiceSerializerResponse


class CommandParameterList(generics.ListAPIView):
    queryset = CommandParameter.objects.all()
    serializer_class = CommandParameterSerializerResponse


class CommandList(generics.ListAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializerResponse


class CommandCreate(generics.CreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializerRequest


class CommandDetail(generics.RetrieveAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializerResponse
