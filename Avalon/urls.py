from django.contrib import admin
from django.urls import path
from Avalon import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('save_register/', views.save_register, name='save_register'),
    path('save_login/', views.save_login, name='save_login'),
    path('open_lobby', views.open_lobby, name="open_lobby"),
    path('create_lobby', views.create_lobby, name='create_lobby'),
    path('open_active_lobbies', views.open_active_lobbies, name="open_active_lobbies"),
    path('join_lobby/<str:lobby_code>/', views.join_lobby, name="join_lobby")
    
]
