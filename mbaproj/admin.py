from django.contrib import admin
from .models import Category, BlogPost
from ckeditor.widgets import CKEditorWidget
from django import forms

from django.utils.translation import gettext_lazy as _

# admin.site.site_header = _("Pandey ji ka beta hu Chumma Chipak Kai leta hu")
admin.site.site_header = _("Climate Change Story Admin")
admin.site.site_title = _("Climate Change Portal")
admin.site.index_title = _("Welcome to the Story of Climate Change Admin")





class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),  # Adding CKEditor widget to the content field
        }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('id', 'title', 'category', 'author', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content', 'author')

