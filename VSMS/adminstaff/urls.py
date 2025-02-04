
from django.urls import path

from .import views

urlpatterns=[
    path('insert/',views.insert,name='inserturl'),
    path('update/<int:stno>',views.update,name='updateurl'),
    path('delete/<int:stno>',views.delete,name='deleteurl'),
    path('select/',views.select,name='selecturl'),
    path('stdget/',views.stdget,name='stdurl'),
    #path('performance/',views.perform,name='performurl'),
    path('getatt/',views.getatt,name='getatturl'),
    path('att/',views.att),
    #path('stdatt/',views.stdatt)
    #path('obj/',views.obj)
    
]