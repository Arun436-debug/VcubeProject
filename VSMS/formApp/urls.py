from django.urls import path

from .import views

urlpatterns =[
    path('insertform/',views.insertform,name='insertformurl'),
    path('select/',views.select),
]