from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("archivos.urls")),
    path("api/gestion/", include("gestion_archivos.urls")),
    path('api/auth/', include('authemail.urls')),
    path("docs/", include_docs_urls(title='Documentacion API repositorio ITSZ', public=True)),

]
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
