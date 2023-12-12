from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Accessory
from .forms import FeedingForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.accessory.all().values_list('id')
    available_accessories = Accessory.objects.exclude(id__in=id_list)
    form = FeedingForm()
    return render(request, 'finches/detail.html', { 
       'finch':finch,
       'feeding_form':form,
       'accessories':available_accessories
        })

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

def add_accessory(request, finch_id, accessory_id):
  Finch.objects.get(id=finch_id).accessory.add(accessory_id)
  return redirect('detail', finch_id=finch_id)

def remove_accessory(request, finch_id, accessory_id):
  Finch.objects.get(id=finch_id).accessory.remove(accessory_id)
  return redirect('detail', finch_id=finch_id)