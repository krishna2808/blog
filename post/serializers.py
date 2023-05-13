from rest_framework import serializers
from .models import Post, Comment, Like


class LikeSerializer(serializers.ModelSerializer):
    """
    LikeSeraiizer is return user and which post user has like post.
    
    """
    username = serializers.SerializerMethodField()
    def get_username(self, obj):
        return obj.user.user_name
    class Meta:
        model = Like
        fields = ('post', 'user', 'username')
        

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    def get_username(self, obj):
        return obj.user.user_name
    
    class Meta:
        model = Comment
        fields = ['id', 'user','username', 'post', 'comment', 'created_datetime', ]
        
class PostSerializer(serializers.ModelSerializer):
    
    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.user.user_name
    
    comment_post = CommentSerializer(many=True, read_only=True)
    like_post = LikeSerializer(many=True, read_only = True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'username', 'title', 'description', 'image', 'created_datetime',  'comment_post' , 'like_post'  ]

# class PostSerializer(serializers.ModelSerializer):

#     username = serializers.SerializerMethodField()
    
#     def get_username(self, obj):
#         return obj.user.user_name
    
#     comment_post = CommentSerializer(many=True, read_only=True)
#     like_post = LikeSerializer(many=True, read_only = True)

    
    # class Meta:
    #     model = Post
    #     fields = ['id', 'user', 'username', 'title', 'description', 'image', 'created_datetime',  'comment_post' , 'like_post'  ]
        
        


        