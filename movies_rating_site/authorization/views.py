from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import CustomUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('authorization:login')
            
    else:
        form = UserRegistrationForm()
    return render(request, 'authorization/register.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            print("Auth passed:", user)
            login(request, user)
            return redirect('main:index')
        messages.error(request, "User not found")
        
    return render(request, 'authorization/login.html') 