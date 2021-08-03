from command.models import Command
from ..serializers import CommandSerializerResponse, CommandSerializerRequest
from rest_framework import generics


class CommandList(generics.ListAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializerResponse


class CommandCreate(generics.CreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializerRequest


class CommandDetail(generics.RetrieveAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializerResponse
