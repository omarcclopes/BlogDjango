from django.urls import path
#from .views import HomeView
from . import views

app_name = 'django_app'

urlpatterns = [
    #pagina inicial
    #path('', HomeView.as_view(), name="home"),
    path('index',views.index, name='index'),
    path('',views.index, name='index'),
    path('teste',views.teste, name='teste'),
    path('posts',views.posts, name='posts'),
    path('novo_post', views.novo_post, name='novo_post'),
    path('novo_autor', views.novo_autor, name='novo_autor'),
    path('novo_categoria', views.novo_categoria, name='novo_categoria'),
    path('edit_post', views.edit_post, name='edit_post'),
    path('edit_post/<int:edit_id>', views.edit_post, name='edit_post')
]

