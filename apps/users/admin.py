from django.contrib import admin
from apps.users.models import User, Liked_product
# Register your models here.
admin.site.register(User)
admin.site.register(Liked_product)