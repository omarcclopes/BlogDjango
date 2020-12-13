from django.contrib import admin

# Register your models here.
from django_app.models import Autor, Post, Categoria

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Post)