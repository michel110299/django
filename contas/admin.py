from django.contrib import admin
from .models import Categoria
from .models import Transacoes

admin.site.register(Categoria)
admin.site.register(Transacoes)