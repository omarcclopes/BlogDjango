from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

@login_required
def posts(request):
    posts = Post.objects.filter(owner=request.user).order_by('id')
    context = {'posts': posts}
    return render(request, 'django_app/posts.html', context)

@login_required
def novo_post(request):
    # ver se a pagina é requisitada pelo metodo POST (VER GET E POST)
    if request.method != 'POST':
        form = PostForm
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            novo_post = form.save(commit=False)
            novo_post.owner = request.user
            novo_post.save()
            return HttpResponseRedirect(reverse('django_app:posts'))
    context = {'form' : form}
    return render(request, 'django_app/novo_post.html', context)

@login_required    
def edit_post(request, edit_id):
    post = Post.objects.get(id=edit_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('django_app:posts'))

    context = {'post' : post, 'form' : form}   
    return render(request, 'django_app/edit_post.html', context)
    
