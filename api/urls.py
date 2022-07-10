from django.urls import path
from . import views

urlpatterns = [
    path('insert', views.api_insert, name="insert"),
    path('show', views.api_show, name="show"),
    path('delete/<int:id>', views.delete,name='delete'),
    path('view/<int:id>', views.view,name='view')

]