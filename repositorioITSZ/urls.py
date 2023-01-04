from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("archivos.urls")),
    path("api/gestion/", include("gestion_archivos.urls")),
    path('api/auth/', include('authemail.urls')),

]
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
