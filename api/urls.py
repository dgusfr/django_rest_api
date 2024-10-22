from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('delete/<int:pk>/', views.deleteItem),  
    path('update/<int:pk>/', views.updateItem), 
]
