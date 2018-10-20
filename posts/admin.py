from django.contrib import admin
from .models import Post, Public, Article, Author, Book


# Register your models here.

admin.site.register(Post)
admin.site.register(Public)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Book)
