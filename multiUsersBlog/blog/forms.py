from django import forms
from django.forms import widgets
from . import models

class PostForm(forms.ModelForm):
    class Meta():
        model=models.Post
        fields=['title','text']
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-texterea post-content'},)
        }
class CommentForm(forms.ModelForm):
    class Meta():
        model=models.Comment
        fields=['text']
        widgets={
            'text':forms.Textarea(attrs={'class':'input-group form-control'}),
            }
