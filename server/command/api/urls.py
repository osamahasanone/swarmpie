from django.urls import path
from .views import *

urlpatterns = [
    path('verb_parameters', VerbParameterList.as_view(),
         name='verb_parameters_list'),
    path('verb_parameters/<int:pk>', VerbParameterList.as_view(),
         name='verb_parameter_retrieve'),
]
