from django import forms

from .models import Post
from .models import Autor
from .models import Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'corpo', 'autor']
        label = {'titulo' : 'Título do Post', 'categoria' : 'Categoria', 'corpo' : '', 'autor' : ' Escrito por '}

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome_autor', 'email_autor']
        label = {'nome_autor' : 'Nome', 'email_autor' : 'e-mail'}

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_cat']
        label = {'nome_cat' : 'Nome'}
