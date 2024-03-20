from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Cinema API",
        default_version='1.0.0',
        description="API documentation" 
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 
        include([
            path('api/', include('api_cinema_root.urls'), name='api_cinema_urls'),
            path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    ]))
]

