from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        user = authenticate(username='admin', password='admin')
        if user is not None:
            return redirect('/home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
        
   
        

