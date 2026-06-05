
from django import forms
from .models import *


class inputform(forms.ModelForm):
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Enter Any URL.....'}))
    

    class Meta:
        model = Mail  
        fields =  '__all__' #['url', 'bahram'] 
