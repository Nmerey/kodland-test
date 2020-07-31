from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_on','slug')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)