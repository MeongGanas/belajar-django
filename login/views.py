from django.shortcuts import render

# Create your views here.


def login_view(request):
    context = {
        "title": "Login"
    }
    return render(request, 'login_view.html', context)
