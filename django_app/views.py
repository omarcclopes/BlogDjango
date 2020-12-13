from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

def index(request):
    dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}
#    return HttpResponse("<h1>Olá mundo, Django!</h1>")
    return render(request, 'django_app/index.html', dicionario_contexto)
    
def teste(request):
    return render(request, 'django_app/teste.html')