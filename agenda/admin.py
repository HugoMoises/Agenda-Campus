from django.contrib import admin
from . models import Local, Evento, Categoria, Atividade, Inscricao, Relatorio

class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1

class RelatorioInline(admin.TabularInline):
    model = Relatorio
    extra = 1 

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'inicio', 'local']
    list_filter = ['local', 'categoria']
    search_fields = ['titulo']

    inlines = [AtividadeInline, RelatorioInline]


admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Atividade)
admin.site.register(Inscricao)
admin.site.register(Relatorio)