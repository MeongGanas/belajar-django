from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from .forms import FormLogin


def login_view(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/login/dashboard')
    return render(request, 'login_view.html', {'form': form})


def dashboard(request):
    context = {
        "title": "Dashboard"
    }
    return render(request, 'dashboard.html', context)
