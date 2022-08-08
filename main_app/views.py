from django.shortcuts import render, redirect
from .models import Item, Material
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', {'items': items})

def items_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  materials_not_needed = Material.objects.exclude(id__in = item.materials.all().values_list('id'))
  return render(request, 'items/detail.html', {'item': item, 'materials': materials_not_needed})

class ItemCreate(CreateView):
  model = Item
  fields = ['task', 'day']
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

def assoc_material(request, item_id, material_id):
  Item.objects.get(id=item_id).materials.add(material_id)
  return redirect('items_detail', item_id=item_id)