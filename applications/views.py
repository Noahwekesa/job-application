from django.shortcuts import HttpResponse, render
from .services import get_all_rows


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


"""

def index(request):
    applications = get_all_rows("Application")
    context = {
        "applications": applications
    }
    return render(request, 'index.html',context)

"""
