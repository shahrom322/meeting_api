from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Meeting API',
        default_version='v1',
    ),
    patterns=[path('api/', include('core.urls'))],
    public=True,
    permission_classes=(permissions.AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', TemplateView.as_view(
        template_name='swaggerui/swaggerui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
