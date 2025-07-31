from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),                  # List + Search
    path('add/', views.book_create, name='book_create'),          # Add a new book
    path('edit/<int:pk>/', views.book_update, name='book_update'),# Update/edit a book
    path('delete/<int:pk>/', views.book_delete, name='book_delete'), # Delete confirmation
]
