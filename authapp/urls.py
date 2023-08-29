from django.urls import path

#From app urls merg to project urls
from authapp import views

urlpatterns = [
    path('signup/',views.SignUp_View,name='signup'),
    path('login/',views.Login_View,name='login'),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
]
