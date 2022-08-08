from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('items/', views.items_index, name='items_index'),
  path('items/<int:item_id>/', views.items_detail, name='items_detail'),
  path('items/create/', views.ItemCreate.as_view(), name='items_create'),
  path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
  path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
  path('materials/create/', views.MaterialCreate.as_view(), name='materials_create'),
  path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='materials_detail'),
  path('materials/', views.MaterialList.as_view(), name='materials_index'),
]