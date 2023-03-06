from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.validators import validate_file_extension
from apps.books.models import Books
# Create your models here.
class User(AbstractUser):
    email = models.EmailField()
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'    
        

class Liked_product(models.Model):
    user = models.ForeignKey(User, related_name='liked_user', on_delete=models.CASCADE)
    product = models.ForeignKey(Books, related_name='liked_product', on_delete=models.CASCADE)   
       
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'       