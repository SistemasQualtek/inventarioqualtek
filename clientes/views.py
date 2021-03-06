from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
import pprint
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import get_user_model
User = get_user_model()

class ClienteList(ListView):
    model = Cliente
    fields = ['id', 'nombre', 'apellidos','email','telefono','celular','empresa','ejecutivo']
class ClienteDetail(DetailView):
    model = Cliente
    fields = ['id', 'nombre', 'apellidos','email','telefono','celular','empresa','ejecutivo']
class ClienteCreation(CreateView):
    model = Cliente
    success_url = reverse_lazy('clientes:list_cliente')
    fields = ['id', 'nombre', 'apellidos','email','telefono','celular','empresa','ejecutivo']
class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = reverse_lazy('clientes:list_cliente')
    fields = ['id', 'nombre', 'apellidos','email','telefono','celular','empresa','ejecutivo']
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:list_cliente')

def principal(request):
    cliente = Cliente.objects.order_by('id')
    template = loader.get_template('home.html')
    context = {
        'cliente': cliente
    }
    return HttpResponse(template.render(context, request))

def cliente(request):
    users = User.objects.all().order_by('id')
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
            return HttpResponseRedirect('/ClienteList')
    else:
        form = ClienteForm()
    template = loader.get_template('clientes/nuevo_cliente.html')
    context = {
        'form': form,
        'users': users

    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/login/')

def ClienteList(request):
    queryset = Cliente.objects.all().order_by('id')
    context = {
        'queryset':queryset
    }
    return render(request, "clientes/cliente_list.html",context)

def ClienteDetail(request,pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	template = loader.get_template('clientes/cliente_detail.html')
	context = {
	'cliente': cliente
	}
	if request.user.is_authenticated():
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/login')
