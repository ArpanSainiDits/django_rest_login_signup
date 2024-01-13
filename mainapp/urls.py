from django.urls import path
from .views import *

urlpatterns = [
    path('register',RegistrationAPIView.as_view(),name="register"),
    path('login',LoginAPIView.as_view(),name="login"),
    path('my',MySecureAPIView.as_view(),name="my"),
]
