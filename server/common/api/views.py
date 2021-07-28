from common.models import Verb
from .serializers import VerbSerializerResponse
from rest_framework import generics


class VerbList(generics.ListAPIView):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializerResponse


class VerbDetail(generics.RetrieveAPIView):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializerResponse
