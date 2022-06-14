from distutils.log import Log
from django.urls import path
from users.views import SignUp, LogIn

urlpatterns = [
    path('/signup', SignUp.as_view()),
]