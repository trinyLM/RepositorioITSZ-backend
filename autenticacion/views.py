from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import AuthTokenSerializer


class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"mensaje": "ha salido de la sesion"}, status=status.HTTP_200_OK)


class SingupView(generics.CreateAPIView):
    serializer_class = UserSerializer
