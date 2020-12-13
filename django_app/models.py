from django.db import models

# Create your models here.
class Autor(models.Model):
    nome_autor = models.CharField(max_length=150)
    email_autor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_autor

class Categoria(models.Model):
    nome_cat = models.CharField(max_length=150)
     
    def __str__(self):
        return self.nome_cat

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, blank=True, null=True)
    corpo = models.TextField(max_length=5000, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.RESTRICT, blank=True, null=True)
    data = models.DateField(db_index=True, auto_now_add=True, null=True)

    def __str__(self):
        return self.titulo
