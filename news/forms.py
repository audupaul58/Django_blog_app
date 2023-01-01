from django import forms
from .models import News


class News_Create_Form(forms.ModelForm):
    
    class Meta:
        model = News
        fields = '__all__'