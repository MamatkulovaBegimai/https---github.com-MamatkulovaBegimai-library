from django.contrib import admin
from apps.books.models import Books, Category

# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_book', 'price', 'category', 'book_pdf', 'book_photo')
    list_display_links = ('name', 'author_book')
    list_editable = ('category',)
 
    
admin.site.register(Category)