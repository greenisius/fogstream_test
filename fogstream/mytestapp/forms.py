from django import forms

from django.core.exceptions import ValidationError
    
class MessageForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)