from django.shortcuts import render
from .services import get_all_rows

def index(request):
    applications = get_all_rows("Application")
    context = {
        "applications": applications
    }
    return render(request, 'index.html',context)
