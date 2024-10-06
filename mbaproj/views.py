from django.shortcuts import render
from .models import Category, BlogPost
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'home.html', {'categories': categories})

def aboutUs(request):
    return render(request, 'aboutus.html')


def contactUs(request):
    return render(request, 'contactUs.html')


def category_blogs(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)  # Get the specific category using the slug
    blogs = BlogPost.objects.filter(category=category)  # Fetch blogs that belong to this category
    return render(request, 'category_blogss.html', {'category': category, 'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blogdetails.html', {'blog': blog})