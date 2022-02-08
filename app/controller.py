from django.shortcuts import render, redirect
from app.model import CarrosForm
from app.models import Carros


def home(request):
    data = {'db': Carros.objects.all()}
    return render(request, 'view.html', data)


def form(request):
    data = {'form': CarrosForm()}
    return render(request, 'add.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {'db': Carros.objects.get(pk=pk)}
    return render(request, 'vi.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'add.html', data)


def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')
