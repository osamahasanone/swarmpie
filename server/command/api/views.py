from command.models import VerbParameter
from .serializers import VerbParameterSerializer
from rest_framework import mixins
from rest_framework import generics


class VerbParameterList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = VerbParameter.objects.all()
    serializer_class = VerbParameterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
