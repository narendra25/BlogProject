from django.contrib import admin

from .models import *
from django.contrib.auth.models import User
# Register your models here.



class contacts(admin.ModelAdmin):
    list_display=['id','name','email','phonenumber','created_at']
admin.site.register(Contacts,contacts)