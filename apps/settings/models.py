from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.FileField(upload_to='logo/')
    phone = models.CharField(max_length=30)
    graphic = models.CharField(max_length=50)
    email = models.EmailField()
    street = models.CharField(max_length=255)
    
    def __str__(self):
        return self.street
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        
class Aboutus(models.Model):
    description_library = models.TextField(max_length=700)
    history = models.TextField(max_length=1000)
    photo_library = models.ImageField(upload_to='photo_library/')

    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        
class Team(models.Model):
    worker_name = models.CharField(max_length=50)
    worker_position = models.CharField(max_length=255)
    worker_photo = models.ImageField(upload_to='photo_employee/')
    facebook = models.URLField()
    twitter = models.URLField()     
    
    def __str__(self):
        return self.worker_name
    
    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Команда' 

class Otklic(models.Model):
    full_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=22)
    subject = models.CharField(max_length=222)
    text = models.TextField(max_length=3333)
    email = models.EmailField()
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'    
    
            