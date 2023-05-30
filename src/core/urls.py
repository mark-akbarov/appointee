from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Appointee API",
        default_version="v1",
        description="Endpoint for Appointee app",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="markakbarov@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/file/', include('file.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
