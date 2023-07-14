from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Halaman Home",
        "active": "index"
    }
    return render(request, 'index.html', context)
