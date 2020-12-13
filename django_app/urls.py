from django.urls import path
from . import views

app_name = 'django_app'

urlpatterns = [
    #pagina inicial
    path('index',views.index, name='index'),
    path('teste',views.teste, name='teste'),
]