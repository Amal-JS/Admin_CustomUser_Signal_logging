from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages

from user_app.models import Custom_User
from . forms import Admin_User_Update_form,Admin_User_Create_form
from . models import LogUser

# Create your views here.

def home(request):
    if not request.user.is_superuser:
        return redirect('admin_app:admin_login')
       
    else:
         # takes all users and all objects in log user model
        users = Custom_User.objects.all()
        log_user_info = LogUser.objects.all()
        print(request.user)
        
    return render(request,'admin_app/home.html',{'users':users,'log_users_info':log_user_info})


def admin_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        '''
        So,here there is two possibillities like first we will check if user is in the built in user model of django
        if found we will check with is_superuser attribute
        if that user has priveliage then will allow to login

        else no user found then it will check with the custom user model and check privelage in there also if found will allow 
        user to login        
        '''

        user = authenticate(request,username = username ,password = password)

        if user :
            if user.is_superuser :
                login(request,user)
                return redirect('admin_app:admin_home')
        elif user is None:

            messages.error(request,"Admin doesn't exist")

            #before creating custom auth backend
            '''try :
                user = Custom_User.objects.get(username = username)
                
                password_matched =user.check_password(password)
                    

                if password_matched:

                    if  user.is_super_user:

                        login(request,user)
                        return redirect('admin_app:admin_home')
                    else:
                        #user exist in custom user model but don't have privelage
                        messages.info(request,"You don't have permissions")

                else:
                    #user exists but wrong password
                    messages.info(request,'Invalid credentials')

            except ObjectDoesNotExist:
                    #no user exists in both built in user and custom user
                    messages.error(request,"Admin doesn't exist")'''

        

    return render(request,'admin_app/admin_login.html')

def admin_logout(request):
    logout(request)
    request.session.flush()
    print(request.session.user)
    return redirect('admin_app:admin_home')
    


def admin_create_user(request):
    if request.method == 'POST':
        form = Admin_User_Create_form(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
           #we want to hash the password before saving it into the db
           
           # user.password=make_password(form.cleaned_data['password'])
            user.password= user.make_password(form.cleaned_data['password'])

            user.save()
            return redirect('admin_app:admin_home')
        else:
            
            
            return render(request,"user_app/user_creation.html",{'form': form})
        
    form = Admin_User_Create_form()
    
    return render(request,"user_app/user_creation.html",{'form': form})



def admin_update_user(request,id):

    #we are getting the object id and passing it to form to get the values already in each field
    user_instance = Custom_User.objects.get(id=id)

    if request.method == 'POST':

        form = Admin_User_Update_form(request.POST,request.FILES,instance = user_instance)
        if form.is_valid():
            form.save()
            return redirect('admin_app:admin_home')
        else:
            
            
            return render(request,"user_app/user_creation.html",{'form': form})
        
    form = Admin_User_Update_form(instance=user_instance)
    
    return render(request,"user_app/user_creation.html",{'form': form})
    



def admin_delete_user(request,id):
    
        user= Custom_User.objects.get(id=id)
        user.delete()
        return redirect('admin_app:admin_home')
    

    