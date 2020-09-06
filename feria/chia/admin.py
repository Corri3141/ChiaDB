from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy
from django.contrib.admin import ModelAdmin, SimpleListFilter,AdminSite
from .models import Cliente, Articulo

class FiltroArticulos(ModelAdmin):
    list_display = ("numero_de_articulo","descripcion","precio","comprador","fecha_de_venta")
    search_fields = ["numero_de_articulo"]

class ArticuloInline(admin.TabularInline):
    model = Articulo


class FiltroClientes(ModelAdmin):
    list_display = ("nombre","apellido","telefono")
    search_fields = ["nombre"]    
    inlines = [ArticuloInline]

admin.site.site_title = "Chia Ferias"
admin.site.site_header = "Chia Ferias!"
admin.site.index_title = "Stock de articulos"

admin.site.register(Cliente,FiltroClientes)
admin.site.register(Articulo,FiltroArticulos)

# Register your models here.
