from command.models import VerbParameter, CommandParameter, Command
from .serializers import *
from rest_framework import generics


class VerbParameterList(generics.ListAPIView):
    queryset = VerbParameter.objects.all()
    serializer_class = VerbParameterSerializer


class CommandParameterList(generics.ListAPIView):
    queryset = CommandParameter.objects.all()
    serializer_class = CommandParameterSerializer


class CommandList(generics.ListAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer


class CommandCreate(generics.CreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandPostSerializer


class CommandDetail(generics.RetrieveAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
