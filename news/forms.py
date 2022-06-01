from django import forms

class NewsLetterForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')