from common.models import Verb
from .serializers import VerbSerializer
from rest_framework import generics


class VerbList(generics.ListAPIView):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializer


class VerbDetail(generics.RetrieveAPIView):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializer
