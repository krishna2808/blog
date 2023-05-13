from rest_framework import serializers
from .models import User
from post.serializers import PostSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField()
    # def get_username(self, obj):
    #     return obj.user_name
    post_user = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_name', 'email', 'first_name', 'last_name', 'image', 'user_about', 'post_user')
        
        