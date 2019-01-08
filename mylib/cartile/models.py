from django.db import models
from django.urls import reverse


class Author(models.Model):
  lastName = models.CharField(max_length=45)
  firstName = models.CharField(max_length=45)
  nationality = models.CharField(max_length=45)

  def get_absolute_url(self):
    return reverse('auth_details', args=[str(self.id)])

  def __str__(self):
    return f'{self.firstName} {self.lastName}'


class Book(models.Model):
  PDF = 'pdf'
  EPUB = 'epub'
  MOBI = 'mobi'
  DOC = 'doc'
  HTML = 'html'
  OTHER = 'other'
  TYPE_CHOICES = (
    (PDF, 'pdf'),
    (EPUB, 'epub'),
    (MOBI, 'mobi'),
    (DOC, 'doc'),
    (HTML, 'html'),
    (OTHER, 'other'),
  )

  author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=128)
  description = models.CharField(max_length=145)
  type = models.CharField(
    max_length=5,
    choices=TYPE_CHOICES,
    default=PDF,
  )
  location = models.CharField(max_length=128)

  def get_absolute_url(self):
    return reverse('book_details', args=[str(self.id)])

  def __str__(self):
    return f'{self.title}'

