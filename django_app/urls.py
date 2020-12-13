from django.urls import path
from . import views

app_name = 'django_app'

urlpatterns = [
    #pagina inicial
    path('',views.index, name='index'),
]