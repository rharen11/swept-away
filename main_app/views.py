from django.shortcuts import render, redirect
from .models import Item, Material
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def items_index(request):
  items = Item.objects.filter(user=request.user)
  return render(request, 'items/index.html', {'items': items})

@login_required
def items_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  materials_not_needed = Material.objects.exclude(id__in = item.materials.all().values_list('id'))
  return render(request, 'items/detail.html', {'item': item, 'materials': materials_not_needed})

class ItemCreate(LoginRequiredMixin, CreateView):
  model = Item
  fields = ['task', 'day']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Item
  fields = ['task', 'day']

class ItemDelete(LoginRequiredMixin, DeleteView):
  model = Item
  success_url = '/items/'

class MaterialCreate(LoginRequiredMixin, CreateView):
  model = Material
  fields = '__all__'

class MaterialList(LoginRequiredMixin, ListView):
  model = Material

class MaterialDetail(LoginRequiredMixin, DetailView):
  model = Material

class MaterialUpdate(LoginRequiredMixin, UpdateView):
  model = Material
  fields = ['name', 'cost']

class MaterialDelete(LoginRequiredMixin, DeleteView):
  model = Material
  success_url = '/materials/'

@login_required
def assoc_material(request, item_id, material_id):
  Item.objects.get(id=item_id).materials.add(material_id)
  return redirect('items_detail', item_id=item_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)