from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Post, Comment

CATEGORIES = [
    ('Criminal Law', 'Criminal Law'),
    ('International Law', 'International Law'),
    ('Labour Law', 'Labour Law'),
    ('Constitutional Law', 'Constitutional Law'),
    ('Corporate Law', 'Corporate Law'),
    ('Property Law', 'Property Law'),
    ('Administrative Law', 'Administrative Law'),
    ('Public Law', 'Public Law'),
    ('Private Law', 'Private Law'),

]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'short_desc', 'cover_image', 'description', 'category']
        widgets={
                   "title":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "short_desc":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "cover_image": forms.FileInput(attrs={'class': 'custom-file-input',}),
                   #"category": forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
                   "category": forms.Select(attrs={'class': 'form-control', 'required': 'required'}, choices=CATEGORIES),
                   "description":forms.TextInput(attrs={'placeholder':'Description','class':'form-control','required':'required'}),
                }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
        widgets={
                   "name":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "email": forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
                   "description":forms.TextInput(attrs={'placeholder':'Description','class':'form-control','required':'required'}),
                }
