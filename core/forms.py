from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class AccoutnForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['owner', 'name', 'balance']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'owner' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'
        