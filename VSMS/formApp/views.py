from django.shortcuts import render

# Create your views here.

from.forms import Stddata,Stdform
from django.contrib import messages
from django.core.paginator import Paginator
from adminstaff.models import Students 
  

def insertform(request):
    stdobj = Stddata()
    if request.method == "POST":
        std = Stddata(request.POST,request.FILES)
        if std.is_valid() == True:
            std.save()
            k = 'Data Inserted Succesfully'
            messages.success(request,k)
            return render(request,'formApp/insert.html',{'stdobj':stdobj})
        else:
            k = 'Something Went Wrong'
            messages.error(request,k)
            return render(request,'formApp/insert.html',{'stdobj':stdobj})
    return render(request,'formApp/insert.html',{'stdobj':stdobj})
        
  
def select(request):
    k = Students.objects.all()
    return render(request,'formApp/select.html',{'sad':k})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    class meta :
        model = User
        fields = ['first_name','username','password1','password2','email','is_superuser']