from django import forms
from .models import *

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

class signupForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model=usersignup
        fields=['firstname','lastname','email','password','cpassword','mobile','dateofbirth','gender','address','adhar']
        
        
        