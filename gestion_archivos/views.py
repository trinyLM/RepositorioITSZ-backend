from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from archivos.models import Archivo
from archivos.serializers import ArchivoSerializer


class ArchivoCreateAPIView(CreateAPIView):
    #permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

class ArchivoUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

class ArchivoDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer






