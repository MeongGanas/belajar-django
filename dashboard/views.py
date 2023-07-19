from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    context = {
        "title": "Dashboard",
        "name": request.user.first_name
    }
    return render(request, 'dashboard.html', context)
