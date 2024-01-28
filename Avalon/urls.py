from django.contrib import admin
from django.urls import path
from Avalon import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('enter_username/', views.enter_username, name='enter_username'),
]
