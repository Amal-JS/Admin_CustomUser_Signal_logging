from django.urls import path
from . import views

app_name = "admin_app"

urlpatterns = [

path('',views.admin_login,name='admin_login'),
path('admin_home/',views.home,name='admin_home'),
path('admin_logout/',views.admin_logout,name='admin_logout'),
path('admin_create_user/',views.admin_create_user,name="admin_create_user"),
path('admin_delete_user/<int:id>/',views.admin_delete_user,name="admin_delete_user"),
path('admin_update_user/<int:id>/',views.admin_update_user,name='admin_update_user'),
path('search_user/',views.search,name='search')


]