from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import FormLogin
from django.conf import settings


def login_view(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/login/dashboard')

    data = {
        'form': form,
        'title': "Login"
    }
    return render(request, 'login_view.html', data)


def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect("/login/")


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    context = {
        "title": "Dashboard",
        "name": request.user.first_name
    }
    return render(request, 'dashboard.html', context)
