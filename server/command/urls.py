from django.urls import path, include

urlpatterns = [
    path('api/', include('command.api.urls'))
]
