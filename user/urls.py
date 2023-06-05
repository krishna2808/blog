
from django.urls import path 
from user import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name='profile'),
    

    # path('', views.sign_up, name='sign_up' ),
    # path('sign_in/', views.sign_in, name='sign_in' ),
    # path('dashboard/', views.dashboard, name='dashboard' ),
    # path('profile/', views.profile, name='profile' ),
    # path('requested_user/', views.requested_user, name='requested_user' ),
    # path('request_accepted/<str:requested_username>/', views.request_accepted, name='request_accepted' ),
    # path('search_user/', views.search_user, name='search_user' ),

    # path('show_user_profile/<str:user_name>/', views.show_user_profile, name='show_user_profile' ),
    # path('follower_following/<str:user_name>/', views.follower_following, name='follower_following'),


    # path('log_out/', views.log_out, name='log_out' ),
           
  
] 