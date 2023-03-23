from django.contrib import admin
from django.urls import path
from KJPL.views import index,menu


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index),
    path('menu',menu),
]
