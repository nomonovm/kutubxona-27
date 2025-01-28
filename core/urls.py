"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world', hello_world),
    path('', home_view, name='home'),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('mualliflar/', mualliflar_view, name='mualliflar'),
    path('mualliflar/<int:muallif_id>/', muallif_details_view),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitoblar/<int:kitob_id>/', kitob_details_view),
    path('recordlar/', recordlar_view, name='recordlar'),
    path("talabalar/<int:pk>/o'chirish/", talaba_delete_view),
    path("talabalar/<int:pk>/o'chirish/tasdiqlash/", talaba_delete_confirm_view),
]
