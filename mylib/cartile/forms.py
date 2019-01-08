from django import forms
from . import models

class CreateAuthor(forms.ModelForm):
  class Meta:
    model = models.Author
    fields = ['firstName', 'lastName', 'nationality']

class CreateBook(forms.ModelForm):
  class Meta:
    model = models.Book
    fields = ['author', 'title', 'description', 'type', 'location']


