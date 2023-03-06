from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='user_profile_image/')
    about_author = models.CharField(max_length=600)
    facebook = models.URLField()
    twitter = models.URLField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        
        