from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="DHAS Swarm",
        default_version='v1',
        description="Tile Communication",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="osama.h@dhas.com.lb"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('commands/', include('command.urls')),
    path('responses/', include('response.urls')),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui')
]
