from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.




def error_404_view(request, exception):
    return render(request, '404.html')

def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    pass

def contact(request):
    pass

def services(request):
    pass

def agnes(request):
        context  = {
        "unit_title" : "The Agnes"
    }
        return render(request, 'mainapp/agnes.html',context)

def ivy(request):
    context  = {
        "unit_title" : "Ivy",
        "unitname" : "ivy"
    }
    return render(request, 'mainapp/ivy.html',context)

def primrose(request):
    context  = {
        "unit_title" : "Primrose",
        "unitname" : "primrose"
    }
    return render(request, 'mainapp/primrose.html',context)

def aurora(request):
    context  = {
        "unit_title" : "Aurora",
        "unitname" : "aurora"
    }
    return render(request, 'mainapp/aurora.html',context)

def emerald(request):
    context  = {
        "unit_title" : "Emerald",
        "unitname" : "emerald"
    }
    return render(request, 'mainapp/emerald.html',context)

def temp(request):
    return render(request, 'mainapp/temp.html')