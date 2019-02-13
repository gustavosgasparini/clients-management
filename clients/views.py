from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def client_logout(request):
    logout(request)
    return redirect('index')


@login_required
def client_list(request):
    clients = Client.objects.order_by('first_name')
    return render(request, 'clients_list.html', {'clients': clients})


@login_required
def client_new(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('client_list')

    return render(request, 'clients_form.html', {'form': form})


@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('client_list')

    return render(request, 'clients_update_form.html', {'form': form})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        client.delete()
        return redirect('client_list')

    return render(request, 'clients_delete_confirm.html', {'client': client})