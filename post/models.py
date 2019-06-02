import os
import random
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from ckeditor.fields import RichTextField
from  ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_file_extension

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_file_path(instance, filename):
    new_filename = random.randint(1, 3231546414654785)
    name, ext =get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "documents/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)




class PostManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Post(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    #text = RichTextField()
    cover_image = models.ImageField(upload_to=upload_file_path, validators=[validate_file_extension], default='images/blog_cover.jpg', blank=True)
    short_desc = models.TextField(max_length=400)
    description = RichTextUploadingField()
    category = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    published = models.BooleanField(default=True)
    fetured = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.title


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, sender=Post)


class Comment(models.Model):
    user = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
