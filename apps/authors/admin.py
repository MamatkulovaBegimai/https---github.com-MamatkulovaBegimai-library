from django.contrib import admin
from apps.authors.models import Authors
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profile_image')
    list_display_links = ('name', 'id')
    list_filter = ('name',)
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="300" height="200">')
    
    def get_image2(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100">')
    
    get_image.short_description = 'Image'
    get_image2.short_description = 'Image'