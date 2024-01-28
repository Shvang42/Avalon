from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'base.html')

def enter_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('active_sessions')  # Redirect to your home page or other page
    return render(request, 'enter_username.html')
