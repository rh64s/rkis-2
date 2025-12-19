from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images', null=True, blank=True)
    text = models.FileField(upload_to='book_text')
    def __str__(self):
        return self.title
    # уникальность
    constraints = [
        models.UniqueConstraint(fields=['title', 'author', 'year', 'publisher'], name='unique_book'),
    ]
