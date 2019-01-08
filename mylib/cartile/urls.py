from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('authors/', views.authors, name='authors'),
  path('books/', views.books, name='books'),
  path('authors/<int:pk>', views.author_details, name='auth_details'),
  path('books/<int:pk>', views.book_details, name='book_details'),
  path('authors/create', views.author_create, name='author_create'),
  path('books/create', views.book_create, name='book_create'),
  path('books/edit/<int:pk>', views.book_edit, name='book_edit'),

]
