from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('user_singup', views.user_singup, name='user_singup'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post', views.post, name='post'),
    path('addpost', views.addpost, name='addpost'),
    path('editpost/<int:id>/', views.editpost, name='editpost'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    
    path('user_logout', views.user_logout, name='user_logout'),
   
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)