from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from core.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'home.html')


def homepage(request):
    return render(request, 'homepage.html')
    
def log_in(request):
    return render(request, 'login.html')
    
    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    
def about(request):
    return render(request, 'about.html')




