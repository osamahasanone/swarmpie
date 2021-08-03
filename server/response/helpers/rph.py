from ..models import ResponseParameterHeader


def get_rph(key):
    return ResponseParameterHeader.objects.filter(key=key).first()
