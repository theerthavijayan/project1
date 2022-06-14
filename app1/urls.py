from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup/',views.signup, name="signup"),
   path('login',views.login, name="login"),
   path('profile',views.profile, name="profile"),
   path('logout',views.logout, name="logout"),

   path('delete/<int:id>', views.delete, name="delete"),
   path('update/<int:id>', views.update, name="update"),
   path('upload', views.upload, name = 'upload'),
   path('check', views.check_name_exist, name='check_name_exist'),
   path('api_ex', views.api_exFn,name='api_ex'),
   path('api_ex/<int:id>', views.api_exFn,name='api_ex'), #delete data by id

   path('stu',views.StuReg, name="stureg"),
]