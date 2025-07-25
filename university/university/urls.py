from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="University API",
        default_version='v1',
        description="University application documentation",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("university/", include("university_api.urls")),
    path("swagger.<format>/", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
