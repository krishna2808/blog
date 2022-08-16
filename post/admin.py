from django.contrib import admin
from .models import Post, Comment, Like 
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_author','post_title', 'post_date')




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment', 'comment_user')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post','like')
    