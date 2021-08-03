from response.models import Response
from ..serializers import ResponseSerializerResponse
from rest_framework import generics


class ResponseList(generics.ListAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializerResponse


class ResponseDetail(generics.RetrieveAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializerResponse
