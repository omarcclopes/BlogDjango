from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'corpo', 'autor']
        label = {'titulo' : 'Título do Post', 'categoria' : 'Categoria', 'corpo' : '', 'autor' : ' Escrito por '}