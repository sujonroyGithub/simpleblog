from django.contrib import admin
from .models import Contact, Post

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'desc', 'image']
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'desc']
