from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('/home') # not implemented

        messages.add_message(request, constants.ERROR, 'Invalid credentials')
        return redirect('/users/login')
    
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password == confirm_password:
            print(1)
            messages.add_message(request, constants.ERROR, 'The passwords must be equal')
            return redirect('/users/register')
        
        if len(password) < 6:
            print(2)
            messages.add_message(request, constants.ERROR, 'The password must have at least 6 characters')
            return redirect('/users/register')
        
        users = User.objects.filter(username=username)

        if users.exists():
            print(3)
            messages.add_message(request, constants.ERROR, 'This user already exists')
            return redirect('/users/register')


        user = User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/users/login')