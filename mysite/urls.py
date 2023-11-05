from django.contrib import admin
from django.urls import path

from main_site import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplatePrincipal.as_view(), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
