from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main:index')
            
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form' : form})