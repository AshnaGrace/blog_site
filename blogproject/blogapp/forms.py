from .models import news
from django import forms
class Todoform(forms.ModelForm):
    class Meta:
        model=news
        fields=['name','img','desc','month','date']