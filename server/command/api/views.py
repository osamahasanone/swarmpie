from command.models import VerbParameter
from .serializers import VerbParameterSerializer
from rest_framework import generics


class VerbParameterList(generics.ListAPIView):
    queryset = VerbParameter.objects.all()
    serializer_class = VerbParameterSerializer
