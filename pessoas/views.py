from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.


def cadastrar_pessoa(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        descricao = request.POST.get('descricao')

    

    data_person = Pessoa(
        nome=nome,
        cep=cep,
        rua=rua,
        bairro=bairro,
        numero=numero,
        descricao=descricao
    )
    

    data_person.save()



    messages.add_message(request, constants.SUCCESS, 'Pessoa cadastrada com sucesso.')
    
    return redirect('/pessoas/dados_pessoa')

    



def dados_pessoa(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.all()
        return render(request, "pessoas.html", {'pessoas':pessoas})
    