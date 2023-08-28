from django.contrib import admin
from django.urls import path,include  #include is the all app urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authapp.urls')),
]
