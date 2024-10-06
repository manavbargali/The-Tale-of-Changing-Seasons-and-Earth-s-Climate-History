from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to ='category')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = "Time Period"  # Singular name in the admin panel
        verbose_name_plural = "Time Periods"  # Plural name in the admin panel

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    feature_img = models.ImageField(upload_to ='blogs')
    content = RichTextUploadingField()  # Use CKEditor rich text field for rich content
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event Occur"  # Singular name in the admin panel
        verbose_name_plural = "Even Occurs"  # Plural name in the admin panel

    def __str__(self):
        return self.title
