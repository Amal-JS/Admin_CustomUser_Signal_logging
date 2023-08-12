from django.shortcuts import redirect, render
from . import forms
from django.contrib import messages
from .models import Custom_User
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate


from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    return render(request,'user_app/index.html')

def create_account(request):

    if request.method == 'POST':

        form = forms.CU_ModelForm(request.POST,request.FILES)

        if form.is_valid():

            user = form.save(commit=False)
           #we want to hash the password before saving it into the db
           
           
            user.password = user.make_password(form.cleaned_data['password'])

            user.save()
            return redirect('user_app:user_login')
        else:
            
            
            return render(request,"user_app/user_creation.html",{'form': form})
        
    form = forms.CU_ModelForm()
    
    return render(request,"user_app/user_creation.html",{'form': form})



def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('user_app:home')
        else:
            messages.info(request,'Invalid credentials')


        """before creating custom auth backend"""
        '''
        try :
            user = Custom_User.objects.get(username = username)
            #this method hashes the given password in the login form and checks the hashed password in the database 
            #returns true if matched else false
            password_matched =user.check_password(password)
            

            if password_matched:
                login(request,user)
                return redirect('user_app:home')
            else:
                messages.info(request,'Invalid credentials')

        except ObjectDoesNotExist:
            messages.error(request,"User doen't exist")'''
        
        
            
    return render(request,'user_app/user_login.html')


def home(request):
    return render(request,'user_app/home.html')