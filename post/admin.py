from django.contrib import admin
from .models import Post, Comment, Like 
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'created_datetime')




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post','comment', 'created_datetime')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post','user')
    