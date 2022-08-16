from statistics import mode
from django.db import models
from user.models import User 
# Create your models here.


class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    post_title = models.CharField(max_length=40)
    pic = models.ImageField(upload_to='images/post/%Y/%m/%d/%T')

    post_discription = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.post_title

     # Change model manager 
    Posts = models.Manager()   
    
    class Meta: 
      ordering = ['-post_date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='comment_user')
    comment = models.CharField(max_length=400)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.post.post_title

    Comments = models.Manager()  
    
    class Meta: 
      ordering = ['-comment_date']

class Like(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  like =  models.ForeignKey(User,on_delete=models.CASCADE )

  Likes = models.Manager() 

class Temp(models.Model):
  name = models.CharField(max_length=20)  
         
