from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name','first_name']

    def __str__(self):
        return f'{self.first_name}{self.last_name}'

class Genre(models.Model):

    genre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.genre}'

class Language(models.Model):

    language = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.language}'

class Book(models.Model):

    title = models.CharField('Title',max_length=30)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language,on_delete=models.SET_NULL,null=True)
    isbn = models.CharField(max_length=10,unique=True,null=False)
    summary = models.TextField()

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.title}'

import uuid
class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    book = models.ForeignKey(Book,on_delete=models.RESTRICT)
    due_back= models.DateField(null = True,blank=True)
    imprint = models.CharField(max_length=20)
    LOAN_STATUS = (
        ('o','on_loan'),
        ('m','maintainance'),
        ('a','available')
    )
    status = models.CharField(max_length = 1,choices=LOAN_STATUS,default='m',null=False)

    def __str__(self):

        return f'{self.id}({self.book.title})'

    



    


