from statistics import mode
from django.db import models
from user.models import User 
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/post/%Y/%m/%d/%T')
    description = models.TextField(null=True, blank=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.title

     # Change model manager 
    Posts = models.Manager()   
    
    class Meta: 
      ordering = ['-created_datetime']



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='comment_post')
    comment = models.CharField(max_length=400, null=True, blank=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.post.title

    Comments = models.Manager()  
    
    class Meta: 
      ordering = ['-created_datetime']


class Like(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE,  related_name='like_post')
  user =  models.ForeignKey(User,on_delete=models.CASCADE , related_name='like_user')
  count = models.IntegerField(default=0)

  Likes = models.Manager() 
  def __str__(self):
    return str(self.count)
