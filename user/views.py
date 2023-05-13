from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


class ProfileView(APIView):
    def get(self, request, format=None):
        user_querset = User.objects.all()
        profile_serializer = UserProfileSerializer(user_querset, many=True)
        return Response(profile_serializer.data, )
















# # function base view 

# from imp import init_builtin
# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from .forms import LoginForm, RegistraionForm, ProfileForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .models import User, Friend
# from post.models import Post, Comment
# from django.urls import reverse


# from django.contrib.auth import authenticate, login, logout 
# from django.db.models import Q


# @login_required(login_url='sign_in')
# def request_accepted(request, requested_username):
#     requested_username = User.objects.get(user_name=requested_username)
#     friend_instance = Friend.objects.get(current_user=requested_username, friend=request.user) 
#     friend_instance.friend_request = 1 
#     friend_instance.save() 
#     return HttpResponseRedirect('/requested_user')
    
    
    
  
# @login_required(login_url='sign_in')
# def follower_following(request, user_name):
#     user = User.objects.get(user_name=user_name)     
    
    
#     following = user.follower.filter(friend_request=1)
#     follower = user.following.filter(friend_request=1)
#     username = User.objects.get(email=str(request.user)).user_name 
    
#     return render(request, 'user/follower_following.html', {'follower': follower, 'following' :following } )
       
   
# @login_required(login_url='sign_in')
# def requested_user(request):
#     request_user_queryset = Friend.objects.filter(friend=request.user, friend_request=0)
    
#     return render(request, 'user/requested_user.html', { 'request_user_queryset': request_user_queryset})
    
    

# @login_required(login_url='sign_in')
# def search_user(request):
#     if request.method == 'POST':
#         search_user = request.POST.get('search_user')
#         if search_user != None: 
#             search_user_instance = User.objects.filter(user_name = search_user).first()
#             if search_user_instance:
#                 search_user_query_instance = User.objects.get(user_name=search_user)
#                 user_name = search_user_query_instance.user_name
#                 # return HttpResponse('yes')
#                 return HttpResponseRedirect('/show_user_profile/' + user_name)
#             messages.warning(request, 'User Not found !')
#     return HttpResponseRedirect('/dashboard')
    

# @login_required(login_url='sign_in')
# def show_user_profile(request, user_name):
#     user = User.objects.get(user_name=user_name)     
#     post_query_set = Post.Posts.filter(post_author=user)
    
#     friend_instance = Friend.objects.filter(Q(current_user=request.user) & Q(friend=user) | Q(current_user=request.user) & Q(friend=user)).first() 
   
#     following = user.follower.filter(friend_request=1).count() 
#     follower = user.following.filter(friend_request=1).count() 
#     username = User.objects.get(email=str(request.user)).user_name 
#     if username == user_name : 
#         return HttpResponseRedirect(reverse('show_own_post'))

#     if request.method == 'POST': 
#         request_id = int(request.POST.get('request_id'))
        
#         if friend_instance: 
#             if  request_id == 0 : 
#                 friend_instance = Friend(current_user=request.user, friend=user, friend_request=request_id)
#                 friend_instance.save() 
#             elif request_id == -1: 
#                 friend_instance = Friend.objects.get(current_user=request.user, friend=user)
#                 friend_instance.delete()
           
                
#         else: 
#             friend_instance = Friend(current_user=request.user, friend=user, friend_request=request_id)
#             friend_instance.save() 
            
#         url = reverse('show_user_profile', kwargs={'user_name': user_name})
#         return HttpResponseRedirect(url)
#     data = { 'user':user, 'user_name' : user_name ,'post_query_set':post_query_set, 'friend_instance' : friend_instance, 'follower' : follower, 'following': following}
#     return render(request, 'user/show_user_profile.html', context=data  )


# @login_required(login_url='sign_in')
# def log_out(request):
#      logout(request)
#      return HttpResponseRedirect('/sign_in')
  

# @login_required(login_url='sign_in')
# def profile(request):
#     title = 'Profile'
#     user = User.objects.get(email=request.user)
   
    
#     if request.method == 'POST': 
#         user.user_about =  request.POST.get('user_about')
#         if len(request.FILES) != 0 :
#             user.image = request.FILES['pic']
#         user.save()
#         messages.success(request, 'Your Profile successfully Updated !')
#     initial_content = {  'user_name': user.user_name, 'email': user.email,  'user_about' :  user.user_about  }
#     form = ProfileForm(initial=initial_content)    
       
#     return render(request, 'user/profile.html', {'form': form , 'title' : title, 'user': user})

# @login_required(login_url='sign_in')
# def dashboard(request):
#     title = 'DashBoard'
#     posts_query_set = Post.Posts.all()

#     return render(request,'user/dashboard.html', {'title': title, 'posts_query_set': posts_query_set, })


# def sign_in(request):
    
    
#     if not request.user.is_authenticated : 
#         title = 'Login'
#         form  = LoginForm()
#         if request.method == 'POST':
#             form =  LoginForm(request.POST)
#             if form.is_valid():
#                 email  = form.cleaned_data['email']
#                 password = form.cleaned_data['password']
#                 user = authenticate(request, email=email , password=password)

#                 if user is not None:
#                     login(request, user)
#                     response = HttpResponseRedirect('/dashboard')   
                                 
#                     return response  
#         # messages.warning(request, 'Please Enter currect details.')    
#         return render(request, 'user/sign_in.html', {'form':form, 'title': title})  
#     return HttpResponseRedirect('/dashboard')
           

# def sign_up(request):
#     form = RegistraionForm()
#     title = 'SignUp'
#     if request.method == 'POST':  
#         form = RegistraionForm(request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['user_name']
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = User.objects.create_user(email=email, name=name, user_name=user_name, password= password)
#             user.save()
#             # messages.success(request, 'Your Account successfully Created !') 
#             form = RegistraionForm()
#             return HttpResponseRedirect('/sign_in')
#         # messages.warning(request, 'Please Enter currect details.')    
#         # else: 
#         #     form = RegistraionForm()
#     return render(request, 'user/sign_up.html' , {'form' :form , 'title': title} )
