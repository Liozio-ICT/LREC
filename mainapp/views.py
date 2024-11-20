from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.




def error_404_views(request):
    pass

def index(request):
    
    return render(request, 'mainapp/index.html')

def about(request):
    pass

def contact(request):
    pass

def services(request):
    pass