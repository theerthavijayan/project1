from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home.html'),
   path('signup/',views.signup, name="signup.html"),
   path('delete/<int:id>  ', views.delete, name="delete"),
]