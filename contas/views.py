from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    listNomes = ['Romulo','michel','lucas','camila','yara']
    context={
        'listNomes':listNomes
    }
   #html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'contas/home.html', context)
