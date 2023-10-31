from django.contrib import admin
from django.urls import path, include
from main_site import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.TemplatePrincipal.as_view(), name='home'),
    path('user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
