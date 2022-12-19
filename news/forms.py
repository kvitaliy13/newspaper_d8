from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['categories',
                 'title',
                 'post_text',
                 'post_author',
                 'event']

