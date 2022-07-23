from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from matplotlib.style import context
from empresa.forms import empresaForm
from empresa.models import empresa
# Create your views here.

def listar(request):
    empresas = empresa.objects.all()
    context = {
        "empresas": empresas
    }
    return render(request, 'empresas/listar.html', context)


def criar(request):
    
    if request.method == "POST":
        form = empresaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/empresa")
    else:
        form = empresaForm()
    
    context ={
        'form': form
    }
    
    return render(request, "empresas/formCriar.html", context)


def excluir(request, empresa_id):
    
    empresa.objects.get(pk=empresa_id).delete()
    
    return HttpResponseRedirect("/empresa")    


def editar(request, empresa_id):
    empresas = empresa.objects.get(pk=empresa_id)
    
    if request.method == "POST":
        form = empresaForm(request.POST, instance=empresas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/empresa")
    else:
        form = empresaForm(instance=empresas)
    
    context ={
        'form': form,
        'empresa_id': empresa_id
    }
    
    return render(request, "empresas/formEditar.html", context)