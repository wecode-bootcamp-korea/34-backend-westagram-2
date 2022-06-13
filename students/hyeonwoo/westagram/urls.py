from django.urls import path, include

urlpatterns = [
    path('westagram', include('users.urls'))
]
