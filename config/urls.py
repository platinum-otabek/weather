from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version='v1',
    ),
    public=False
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger')
]
