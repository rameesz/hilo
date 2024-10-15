from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_fruit_set, name='add_fruit_set'),
    path('search/', views.search_fruit_set, name='search_fruit_set'),
    path('view/<int:id>/', views.view_fruit_set, name='view_fruit_set'),
    path('edit/<int:id>/', views.edit_fruit_set, name='edit_fruit_set'),
    path('list-fruit-sets/', views.list_fruit_sets, name='list_fruit_sets'),
]
