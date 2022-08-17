


# ---------------------------- Package import ----------------------------------


from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import AddPost, EditPost
from .models import Post, Comment, Like 
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import View


#class base view 

# Class base View ------------------------------------------------------

class AddPostView(LoginRequiredMixin, View):
    login_url = 'sign_in'

   
    def get(self, request):
        form = AddPost()
        return render(request, 'post/add_post.html', {'form': form, 'title': 'Add Post'})

    def post(self, request):
        form = AddPost(request.POST)
        if request.POST.get('pic') != ''  and request.POST.get('post_title') and request.POST.get('post_discription') != ''     :
            # user_name  = request.COOKIES['user_name']
            user_model_instance = User.objects.get(email=request.user )
            if user_model_instance:                
                post = Post(post_author=user_model_instance, post_title = request.POST.get('post_title'), pic=request.FILES.get('pic')  , post_discription = request.POST.get('post_discription')).save()
                messages.success(request, 'Your Post successfully Added !')
             
                return HttpResponseRedirect('/post/add_post')
        return render(request, 'post/add_post.html', {'form': form, 'title': 'Add Post'})




class ShowOwnPost(LoginRequiredMixin, View):
    login_url = 'sign_in'
    
    def get(self, request):
        user_model_instance = User.objects.get(email=request.user)
        post_query_set = Post.Posts.filter(post_author = user_model_instance)
        following = user_model_instance.follower.filter(friend_request=1).count() 
        follower = user_model_instance.following.filter(friend_request=1).count() 
        user_name = user_model_instance.user_name
        print(following, follower, 'folower follwing ****** ')
        data = {'post_query_set': post_query_set, 'user_name': user_name,  'title': 'Show Your Post', 'user' : user_model_instance, 'follower' : follower, 'following': following}
        return render(request, 'post/show_own_post.html', context=data )




class EditDeletePost(LoginRequiredMixin, View):
    login_url = 'sign_in'

    def get(self, request, post_id):
        post_instance = Post.Posts.get(id=post_id)
        initial_content = { 'post_title': post_instance.post_title, 'post_discription' :  post_instance.post_discription }
        form = EditPost(initial_content)
        return render(request, 'post/edit_delete_post.html', {'form': form, 'title': 'Edit & Delete Post', 'post': post_instance})
    def post(self, request, post_id):
        form = EditPost(request.POST)
        post_instance = Post.Posts.get(id=post_id)
        if form.is_valid():
            title = form.cleaned_data['post_title']
            discription = form.cleaned_data['post_discription']
            post_instance = Post.Posts.get(id=post_id)
            post_instance.post_title = title
            post_instance.post_discription = discription
            post_instance.save()
            messages.success(request, 'Your Post successfully Updated !')
            return render(request, 'post/edit_delete_post.html', {'form': form, 'title': 'Edit & Delete Post', 'post': post_instance})
        

        data = {'form': form, 'title': 'Edit & Delete Post', 'post': post_instance}
        return render(request, 'post/edit_delete_post.html', context=data )

   

class CommentView(LoginRequiredMixin, View):
        login_url = 'sign_in'
        def get(self,request, post_id):
            post_instance = Post.Posts.get(id=post_id)

            comment_query_set = Comment.Comments.filter(post=post_instance)
            data = {'comment_query_set': comment_query_set, 'post_id' : post_id, }

            return render(request, 'post/show_comments.html', context=data)

        def post(self,request, post_id): 
            post_instance = Post.Posts.get(id=post_id)
            user_instance = User.objects.get(email=request.user)
            comment = request.POST.get('comment')
            comment_query_set = Comment.Comments.filter(post=post_instance)
            if comment != '':
                comment_instance = Comment(post=post_instance, comment=comment, comment_user=user_instance)
                comment_instance.save()
                messages.success(request, 'Your Comment successfully Added !')
            else:
                messages.warning(request, 'Add Comment First ')
            
            data= {'comment_query_set': comment_query_set, 'post_id' : post_id, }
            return render(request, 'post/show_comments.html',context=data)
        
        
        


class LikeView(View):
    
    def get(self, request, post_id):
        title = 'show likes'
        post_instance = Post.Posts.get(id=post_id)
        like_counter = Like.Likes.filter(post=post_instance).count()
        
        like_query_set = Like.Likes.filter(post=post_instance)
        data = {'title': title, 'count': like_counter, 'like_query_set':like_query_set}
        return render(request, 'post/show_likes.html', context=data)
                      

def delete_post(request, post_id):
    delete_post_instance = Post.Posts.get(id=post_id)
    if delete_post:
        delete_post_instance.delete()
        messages.success(request, 'Your Post successfully Deleted !') 
    return HttpResponseRedirect('/post/show_own_post')    
   
        
