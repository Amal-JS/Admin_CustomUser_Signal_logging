from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [

path('login_User',views.user_login,name='user_login'),#login user url
path('create_account/',views.create_account,name='create_account'),

path('',views.index,name='index'), #application index page

path('home/',views.home,name='home') #application home page


]