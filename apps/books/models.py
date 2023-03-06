from tabnanny import verbose
from django.db import models
from apps.authors.models import Authors
# Create your models here.
class Category(models.Model):
    category_books = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name="Человекопонятный URL", blank=True, null=True)
    
    def __str__(self):
        return self.category_books
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Books(models.Model):
    name = models.CharField(max_length=100)
    author_book = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='author_book')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_book',blank=True, null=True)
    pages = models.CharField(max_length=2000)
    format = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    publication_date = models.DateField()
    book_photo = models.ImageField(upload_to='books_photo/')
    dimensions = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    book_description = models.TextField(max_length=2000)
    book_pdf = models.FileField(upload_to ='books_pdf')
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        

    
            
        
    