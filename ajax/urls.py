from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg_page, name='reg'),
    path('register', views.register, name='register'),
    path('display', views.display, name='display'),
    path('displaydata', views.displaydata, name='displaydata'),
    path('deletedata', views.deletedata,name='deletedata'), 
    path('updatedata', views.updatedata,name='updatedata'),     
    path('update', views.update,name='update'),     
    path('check', views.check_user,name='check'),     
    # path('home', views.home   )
]