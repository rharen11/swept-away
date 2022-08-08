from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Item:
  def __init__(self, task, date):
    self.task = task
    self.date = date

items = [
  Item('bathroom', '3/3/22'),
  Item('kitchen floor', '5/6/22'),
  Item('desk', '6/12/22')
]

def items_index(request):
  return render(request, 'items/index.html', {'items': items})
