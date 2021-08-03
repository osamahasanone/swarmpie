from django.urls import path
from .views import *

urlpatterns = [
    path('verbs', VerbList.as_view(), name='verbs_list'),
    path('verbs/<int:pk>', VerbDetail.as_view(),
         name='verb_retrieve'),
]
