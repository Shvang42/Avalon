from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .models import Lobby
from datetime import datetime 
from random import randint
def home(request):
    return render(request, 'base.html')

def register(request):
    return render(request, "register.html")
    

def save_register(request):
    if request.method == "POST":
        if "user_id" in request:
            render(request, "base.html")

        username = request.POST.get('username')
        if len(str(username)) < 25:
            user_id = ""
            for _ in range(25):
                user_id += chr(randint(97, 122))
            user = User(username=username, user_id=user_id)
            user.save()
            request.session["username"] = username 
            request.session["user_id"] = user_id 
            print("SUCCESS!")
    users = User.objects.all()
    for user in users:
        print(user.username)
        
        
    return render(request, "base.html")

def open_lobby(request):
    return render(request, "create_lobby.html")

def create_lobby(request):
    if request.method == "POST":
        if "user_id" not in request.session:
            print("MUST CREATE USER FIRST")
            return render(request, "base.html")
        lobby_name = request.POST.get("name")
        lobby_code = request.POST.get("code")
        user_id = request.session['user_id']
        request.session["lobby_name"] = lobby_name
        request.session["lobby_code"] = lobby_code 
      

        if "username" not in request.session:
            username = ""
            for _ in range(10):
                username += chr(randint(97, 122))
        else:
            username = request.session["username"]
        
        
        lobbys = Lobby.objects.all()
        for lobby in lobbys:
            print(lobby.lobby_name, lobby.lobby_code)
            if lobby.lobby_code == lobby_code:
                return render(request, "error.html")
        lobby = Lobby(lobby_name=lobby_name, lobby_code=lobby_code, lobby_host=username, lobby_host_id=user_id)

       
        lobby.lobby_users.append((username, user_id))
        lobby.save()
        rel_lobby = lobby 
        return render(request, "lobby.html", {"lobby" : rel_lobby})
    
def open_active_lobbies(request):
    lobbies = Lobby.objects.all()
    
    return render(request, "active_sessions.html", {'lobbies' : lobbies})

def join_lobby(request, lobby_code):
    if "username" not in request.session:
        return render(request, "base.html")
    username = request.session['username']
    user_id = request.session['user_id']
    lobbies = Lobby.objects.all()
    rel_lobby = None
    print(username, lobby_code, "??????")
    for lobby in lobbies:
        print(lobby.lobby_code)
        if lobby.lobby_code == lobby_code:
            rel_lobby = lobby
            if (username, user_id) not in lobby.lobby_users:
               
                rel_lobby.lobby_users.append((username, user_id))
    if rel_lobby:
        print(rel_lobby.lobby_users)
        rel_lobby.save()
    
    return render(request, "lobby.html", {'lobby' : rel_lobby})
    

