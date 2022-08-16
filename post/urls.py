
from django.urls import path 
from post import views

# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('add_post/', views.add_post, name='add_post' ),
    path('add_post/', views.AddPostView.as_view(), name='add_post' ),
    path('show_own_post/', views.ShowOwnPost.as_view(), name='show_own_post' ),
    path('edit_delete_post/<int:post_id>/', views.EditDeletePost.as_view(), name='edit_delete_post' ),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post' ),
    path('show_comments/<int:post_id>/', views.CommentView.as_view(), name='show_comments' ),
    path('show_likes/<int:post_id>/', views.LikeView.as_view(), name='show_likes' ),

   
             
  
] 
