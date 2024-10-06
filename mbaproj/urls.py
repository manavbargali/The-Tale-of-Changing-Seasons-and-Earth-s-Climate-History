from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutUs/', views.aboutUs, name='aboutus'),
    path('contactUs/', views.contactUs, name='contactus'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blogs/<slug:category_slug>/', views.category_blogs, name='category_blogs'),  
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
