
from django.contrib import admin
from django.urls import path, include
# from user.views import sign_in, sign_up
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')), 
    path('', include('post.urls')), 
   

]  +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
