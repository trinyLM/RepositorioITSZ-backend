from django.urls import path
from .views import LogoutView, SingupView
from .views import LoginView

urlpatterns = [
    # Auth views
    path("login/", LoginView.as_view(), name="login"),
    path('logout/',
         LogoutView.as_view(), name='logout'),
    path('singup/',
         SingupView.as_view(), name='singup'),

]
