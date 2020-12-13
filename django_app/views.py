from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

def index(request):
#    return HttpResponse("<h1>Olá mundo, Django!</h1>")
    return render(request, 'django_app/index.html')