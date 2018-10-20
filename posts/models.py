from django.db import models


# Create your models here.
class Book(models.Model):
       price = models.IntegerField()
       pages = models.IntegerField(null=False, default="250")

class Author(models.Model):
       name = models.CharField(max_length=200, choices="")
       price = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

class Post(models.Model):
    title = models.CharField(max_length=250, primary_key=True)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='pictures/')
    body = models.TextField(null=False)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def pub_date_shortcut(self):
        return self.pub_date.strftime('%b %e %Y')

    def body_shortcut(self):
        return self.body[:100]

    @staticmethod
    def x(y, z):
        return y + z


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publication = models.ManyToManyField('Public')

    def __str__(self):
        return self.headline


class Public(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "reshu"










