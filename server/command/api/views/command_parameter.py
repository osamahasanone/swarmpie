from command.models import *
from ..serializers import *
from rest_framework import generics


class CommandParameterList(generics.ListAPIView):
    queryset = CommandParameter.objects.all()
    serializer_class = CommandParameterSerializerResponse
