from django import forms

from .models import Post

class PostCreateForm(forms.Form):
    title=forms.CharField()
    body=forms.CharField()

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"


