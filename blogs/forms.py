from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.Form):
    class Meta:
        model = Post
        exclude = ("views",)