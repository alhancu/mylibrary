from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Author, Book
from  . import forms

def index(request):
  num_auths = Author.objects.all().count()
  num_books = Book.objects.all().count()
  auth_list = Author.objects.all()
  context = {
    'num_auths': num_auths,
    'num_books': num_books,
    'authors': auth_list,
  }
  return render(request, 'cartile/index.html', context)

def authors(request):
  auth_list = Author.objects.all()
  context = {'authors': auth_list }
  return render(request, 'cartile/authors.html', context)


def books(request):
  book_list = Book.objects.all()
  context = {'books': book_list }
  return render(request, 'cartile/books.html', context)

def author_details(request, pk):
  auth = get_object_or_404(Author, pk=pk)
  context = {'author': auth}
  return render(request, 'cartile/auth_details.html', context)


def book_details(request, pk):
  book = get_object_or_404(Book, pk=pk)
  context = {'book': book}
  return render(request, 'cartile/book_details.html', context)

def author_create(request):
  if request.method == 'POST':
    form = forms.CreateAuthor(request.POST)
    if form.is_valid():
      # save to DB
      form.save()
      return redirect('authors')
  else:
    form = forms.CreateAuthor()
  return render(request, 'cartile/author_create.html', {'form': form})

def book_create(request):
  if request.method == 'POST':
    form = forms.CreateBook(request.POST)
    if form.is_valid():
      # save to DB
      form.save()
      return redirect('books')
  else:
    form = forms.CreateBook()
  return render(request, 'cartile/book_create.html', {'form': form})

# def book_edit(request, pk):
#   pass

class BookDetailView(generic.DetailView):
  model = Book
