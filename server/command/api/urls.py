from django.urls import path
from .views import *

urlpatterns = [
    path('verb_parameters', VerbParameterList.as_view(),
         name='verb_parameters_list'),
    path('command_parameters', CommandParameterList.as_view(),
         name='command_parameters_list'),
    path('commands', CommandList.as_view(), name='commands_list'),
    path('commands/<int:pk>', CommandDetail.as_view(),
         name='command_retrieve'),
]
