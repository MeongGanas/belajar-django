from django.shortcuts import render

# Create your views here.


def contact(request):
    context = {
        "title": "Halaman Contact",
        "active": "contact"
    }
    return render(request, 'contact.html', context)
