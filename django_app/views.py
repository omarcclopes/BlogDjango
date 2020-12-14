from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import PostForm

# Create your views here.
#from django.http import HttpResponse

def index(request):
    dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}
#    return HttpResponse("<h1>Olá mundo, Django!</h1>")
    return render(request, 'django_app/index.html', dicionario_contexto)
    
def teste(request):
    return render(request, 'django_app/teste.html')

def posts(request):
    posts = Post.objects.order_by('titulo')
    context = {'posts': posts}
    return render(request, 'django_app/posts.html', context)

def novo_post(request):
    # ver se a pagina é requisitada pelo metodo POST (VER GET E POST)
    if request.method != 'POST':
        form = PostForm
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('django_app:posts'))
    context = {'form' : form}
    return render(request, 'django_app/novo_post.html', context)
    
def edit_post(request, edit_id):
    post = Post.objects.get(id=edit_id)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('django_app:posts'))

    context = {'post' : post, 'form' : form}   
    return render(request, 'django_app/edit_post.html', context)
    
