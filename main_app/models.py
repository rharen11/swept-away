from django.db import models
from django.urls import reverse

class Item(models.Model):
  task = models.CharField(max_length=100)
  day = models.CharField(max_length=20)

  def __str__(self):
    return self.task

  def get_absolute_url(self):
      return reverse("items_detail", kwargs={"item_id": self.id})
  
  
