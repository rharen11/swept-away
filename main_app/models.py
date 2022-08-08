from django.db import models
from django.urls import reverse

class Material(models.Model):
  name = models.CharField(max_length=100)
  cost = models.IntegerField(max_length=10)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("materials_detail", kwargs={"pk": self.id})

class Item(models.Model):
  task = models.CharField(max_length=100)
  day = models.CharField(max_length=20)
  materials = models.ManyToManyField(Material)

  def __str__(self):
    return self.task

  def get_absolute_url(self):
      return reverse("items_detail", kwargs={"item_id": self.id})
  
  
  
