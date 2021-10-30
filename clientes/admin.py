from django.contrib import admin
from .models import Person, Documentos, Venda, Produto


admin.site.register(Person)
admin.site.register(Documentos)
admin.site.register(Venda)
admin.site.register(Produto)

