from django import forms
from .models import Post, Comment


class Post_Create_Form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
        
        

class Comment_Form(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'post',
            'author',
            'body',
           
        ]