from django.contrib import admin
from contas.models import Categoria
from contas.models import Transacao

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Transacao)
