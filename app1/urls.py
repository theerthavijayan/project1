from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup/',views.signup, name="signup"),

   path('delete/<int:id>', views.delete, name="delete"),
]