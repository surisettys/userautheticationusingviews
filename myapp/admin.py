from django.contrib import admin
from myapp.models import Book,BookInstance,Author,Genre,Language

# Register your models here.

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
