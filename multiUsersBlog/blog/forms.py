from django import forms
from django.forms import widgets
from . import models

class PostForm(forms.ModelForm):
    class Meta():
        model=models.Post
        fields=['title','text']
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass form-control  col-xs-2' ,'aria-label':"Small", 'aria-describedby':"inputGroup-sizing-sm"}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-texterea post-content form-control col-sm ' ,'aria-label':"Small", 'id':"exampleFormControlTextarea1" , 'rows':"3"},)
        }
class CommentForm(forms.ModelForm):
    class Meta():
        model=models.Comment
        fields=['text']
        widgets={
            'text':forms.Textarea(attrs={'class':'input-group form-control'}),
            }
