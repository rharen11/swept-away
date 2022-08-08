from django.shortcuts import render
from .models import Item, Material
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', {'items': items})

def items_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  return render(request, 'items/detail.html', {'item': item})

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/items/'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['task', 'day']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'

class MaterialCreate(CreateView):
  model = Material
  fields = '__all__'

class MaterialList(ListView):
  model = Material

class MaterialDetail(DetailView):
  model = Material

class MaterialUpdate(UpdateView):
  model = Material
  fields = ['name', 'cost']

class MaterialDelete(DeleteView):
  model = Material
  success_url = '/materials/'