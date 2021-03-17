from django.shortcuts import render , redirect
from django.http import HttpResponse
import datetime
from .models import Transacoes
from .form import Transacoesform, CategoriaForm

def home(request):

    data = datetime.datetime.now()


    listNomes = ['Romulo','michel','lucas','camila','yara']
    context={
        'listNomes':listNomes,
        'data':data,
    }
    return render(request,'contas/home.html', context)
def listagem(request):   
    context={
        'trasacoes':Transacoes.objects.all(),
    }

    return render(request,'contas/listagem.html',context)
def nova_transacao(request):

    form = Transacoesform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    context = {

        'form':form,
    }


    return render(request,'contas/form.html',context)

def nova_categoria(request):

    formCat = CategoriaForm(request.POST or None)

    if formCat.is_valid():
        formCat.save()
        return redirect('url_nova')

    context = {
        'formCat':formCat,
    }


    return render(request,'contas/formCat.html',context) 

def update(request,pk):
    transacao = Transacoes.objects.get(pk=pk)
    form = Transacoesform(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    context = {

        'form':form,
        'transacao' : transacao,
    }


    return render(request,'contas/form.html',context)

def delete(request,pk):
    transacao = Transacoes.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')

