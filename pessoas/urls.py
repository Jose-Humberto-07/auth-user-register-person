from django.urls import path

from . import views

urlpatterns = [
    path("cadastrar_pessoa/", views.cadastrar_pessoa, name="cadastrar_pessoa"),
    path("dados_pessoa/", views.dados_pessoa, name="dados_pessoa")
  
]