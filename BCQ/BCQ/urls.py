from django.contrib import admin
from django.urls import path
from BCQ.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',login),
]
