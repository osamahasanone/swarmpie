from command.models import VerbParameter, CommandParameter, Command
from .serializers import VerbParameterSerializer, CommandParameterSerializer, CommandSerializer
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


class CommandDetail(generics.RetrieveAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
