from django import forms
from . models import Movies

class movieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','desc','year','m_desc','img']