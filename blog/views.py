from django.shortcuts import render

# Create your views here.


def blog(request):
    context = {
        "title": "Blog",
    }
    return render(request, 'blog.html', context)
