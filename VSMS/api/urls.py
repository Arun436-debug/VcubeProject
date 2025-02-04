
from django.urls import path
from .import views

urlpatterns = [

    path('getstddata/<int:stno>/',views.stddataa,name='geturl'),
    path('restget/',views.reststd,name='selecturl'),
    path('restupdate/<int:stno>/',views.restupdate,name='updateurl'),
    path('getatt/<int:rnum>/',views.getatt,name='getatturl'),
    path('att/',views.att,name='atturl'),
    path('insertform/',views.insertform,name='inserturl'),
    path('login/',views.login,name='loginurl'),
    path('logout/',views.logout,name='logouturl'),
    #path('attupdate/<int:stno>/ ',views.attupdate) 

]

