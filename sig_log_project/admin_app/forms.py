'''
so in the user_app form there we are actually hiding the is_super_user attribute 
but in admin , admin can have the choice of changing the fields of user and can also make the user to super_user so for that here we are
again creating form


'''

from user_app.models import Custom_User
from django import forms




class Admin_User_form(forms.ModelForm):

    #to get label pass it like an argument
    #to get password input , use widget and specified passwordinput it like an argument
    
   
    # this is boolean field so it will have value either 'True' or 'False' . the widget for that is checkbox 
    # and this a checkbox so we need label for it 
    is_super_user = forms.BooleanField(label='Super User', widget=forms.CheckboxInput(attrs={'class': 'mx-2',}),required=False)

    class Meta:

        model = Custom_User

        fields = ['username',  'is_super_user', 'phone_number', 'email']

        widgets = {
            

            

            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),

            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Phone number'}),

            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),

           
            

        }

       

