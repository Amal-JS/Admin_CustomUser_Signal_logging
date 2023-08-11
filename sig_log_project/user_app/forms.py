from django import forms
from . import models
from django.core.exceptions import ValidationError

#creating model form for Custom User model


class CU_ModelForm(forms.ModelForm):

    #to get label pass it like an argument
    #to get password input , use widget and specified passwordinput it like an argument
    
    password2 = forms.CharField(max_length=30 ,label ='Confirm Password' ,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = models.Custom_User
        fields = ['username', 'password','password2', 'phone_number', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'type': 'password','placeholder':'Enter Password'}),

            #will not work because the password2 is not a filed in CustomUser model
            #'password2': forms.PasswordInput(attrs={'type': 'password'}),
            #to get password input in html , we have passed widget=forms.PasswordInput at field declartion

            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Phone number'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
            

        }
       

    #compare passwords
    def clean_password2(self):
        value2 = self.cleaned_data['password2']
        value1 = self.cleaned_data['password']
        if value1 != value2:
            raise ValidationError("Passwords didn't match")
        return value2
    

    