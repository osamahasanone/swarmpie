from command.models import CommandParameter
from ..serializers import CommandParameterSerializerResponse
from rest_framework import generics


class CommandParameterList(generics.ListAPIView):
    queryset = CommandParameter.objects.all()
    serializer_class = CommandParameterSerializerResponse
