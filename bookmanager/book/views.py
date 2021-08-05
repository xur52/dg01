from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest

def index(request):
    context = {
        'name': 'Rui Xu'
    }

    return render(request, 'book/index.html', context= context )
