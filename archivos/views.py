
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .models import Archivo
from .serializers import ArchivoSerializer
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ArchivoList(generics.ListAPIView):
    """Vista que lista todos los archivos"""
    # AUTENTICACION
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    #def get(self, request, format=None):
     #   content = {
      #      'user': str(request.user),  # `django.contrib.auth.User` instance.
       #     'auth': str(request.auth),  # None
        #}
        #return Response(content)
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'materia', 'fecha_publicacion']


class ArchivoListDetail(generics.RetrieveAPIView):

    # AUTENTICACION
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'materia', 'fecha_publicacion']
