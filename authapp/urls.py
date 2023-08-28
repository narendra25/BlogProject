from django.urls import path

#From app urls merg to project urls
from authapp import views

urlpatterns = [
    path('signup/',views.SignUp_View)
]
