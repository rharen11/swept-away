from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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