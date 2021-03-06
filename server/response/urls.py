from django.urls import path
from .views import *

urlpatterns = [
    path('response_parameters', ResponseParameterList.as_view(),
         name='response_parameters_list'),
    path('', ResponseList.as_view(), name='responses_list'),
    path('<int:pk>', ResponseDetail.as_view(),
         name='response_retrieve'),
]
