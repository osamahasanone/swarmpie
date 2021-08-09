from command.models import VerbParameter
from ..serializers import VerbParameterSerializerResponse
from rest_framework import generics


class VerbParameterList(generics.ListAPIView):
    queryset = VerbParameter.objects.all()
    serializer_class = VerbParameterSerializerResponse
