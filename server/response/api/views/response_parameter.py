from response.models import ResponseParameter
from ..serializers import ResponseParameterSerializerResponse
from rest_framework import generics


class ResponseParameterList(generics.ListAPIView):
    queryset = ResponseParameter.objects.all()
    serializer_class = ResponseParameterSerializerResponse
