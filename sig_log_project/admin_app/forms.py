'''
so in the user_app form there we are actually hiding the is_super_user attribute 
but in admin , admin can have the choice of changing the fields of user and can also make the user to super_user so for that here we are
again creating form


'''

from user_app.models import Custom_User
from django import forms




class Admin_User_Update_form(forms.ModelForm):

    #to get label pass it like an argument
    #to get password input , use widget and specified passwordinput it like an argument
    
   
    # this is boolean field so it will have value either 'True' or 'False' . the widget for that is checkbox 
    # and this a checkbox so we need label for it 
    is_superuser = forms.BooleanField(label='Super User', widget=forms.CheckboxInput(attrs={'class': 'mx-2',}),required=False)

    class Meta:

        model = Custom_User

        fields = ['username',  'is_superuser', 'phone_number', 'email']

        widgets = {
            

            

            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),

            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Phone number'}),

            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),

           
            

        }

       


class Admin_User_Create_form(forms.ModelForm):

    #to get label pass it like an argument
    #to get password input , use widget and specified passwordinput it like an argument
    
    password2 = forms.CharField(max_length=30 ,label ='Confirm Password' ,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = Custom_User
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
            raise forms.ValidationError("Passwords didn't match")
        return value2
    

    