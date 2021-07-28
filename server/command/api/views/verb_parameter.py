from command.models import *
from ..serializers import *
from rest_framework import generics


class VerbParameterList(generics.ListAPIView):
    queryset = VerbParameter.objects.all()
    serializer_class = VerbParameterChoiceSerializerResponse
