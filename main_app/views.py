from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Swept Away</h1>')

def about(request):
  return HttpResponse('<h1>Welcome to Swept Away! You will clean yourself happy</h1>')
