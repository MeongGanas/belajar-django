from django.shortcuts import render

# Create your views here.


def blog(request):
    context = {
        "title": "Halaman Blog"
    }
    return render(request, 'blog.html', context)