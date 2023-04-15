from django.contrib import admin
from django.urls import path , include
from rest_framework import routers, serializers, viewsets
from user.views import MenberViewSet

from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'menbers', MenberViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

