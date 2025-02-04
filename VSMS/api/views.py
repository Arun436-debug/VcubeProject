from django.shortcuts import render , redirect
#from django.http import JsonResponse
from adminstaff.models import Students
from api.serializer import StudentSerializer,AttendenceSerializer,FormSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from adminstaff.models import Attendence
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#import json

'''
def stddata(request):
    data = {'stdno':1,'stdname':'Arun Kumar','Batch':'Django-13'}

    output = json.dumps(data)

    return JsonResponse(output,safe=False)
'''
@api_view(['GET'])
#@login_required(login_url='loginurl')
def stddataa(request,stno):
    if request.method == "GET":
        s = Students.objects.filter(stdno=stno)
        st = StudentSerializer(s,many=True)
        return Response(st.data,HTTP_200_OK)
        
    
@api_view(['GET','POST'])
#@login_required(login_url='loginurl')
def reststd(request):
    stddata = Students.objects.all()
    if request.method == "POST":
        stdobj = StudentSerializer(data=request.data)
        print(stdobj)
        if stdobj.is_valid():
            stdobj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    else:
        stndobj = StudentSerializer(stddata,many = True)
        return Response(stndobj.data,status=HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
#@login_required(login_url='loginurl')
def restupdate(request,stno):
        stdobj = Students.objects.get(stdno=stno)
        if request.method == 'PUT':
            sget = StudentSerializer(stdobj,data=request.data)
            if sget.is_valid() == True:
                sget.save()
                return Response(status=HTTP_200_OK)
            else:
                return Response(status=HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            stdobj.delete()
            return Response(status=HTTP_200_OK)
        else:
            s = StudentSerializer(stdobj)
            return Response(s.data,status=HTTP_200_OK)
    #return render(request,'vsms/restupdate.html')
'''
@api_view(['GET','PUT','DELETE'])
def attupdate(request,stno):
    a = Attendence.objects.filter(rollnum=stno)
    if request.method == 'GET':
        at = AttendenceSerializer(a,many=True)
        return Response(at.data,status=HTTP_200_OK)        
    elif request.method == "PUT":
        A = AttendenceSerializer(data=request.data)
        if A.is_valid():
            A.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)        

    else:
        a.delete()
        return Response(status=HTTP_200_OK)
'''

@api_view(['GET','POST','PUT'])
#@login_required(login_url='loginurl')
def getatt(request,rnum):
    atrnum = Attendence.objects.filter(rollnum=rnum)
    #st = Students.objects.get(stdno=rnum)
    if request.method == "POST":
        atdobj = AttendenceSerializer(data=request.data)
        if atdobj.is_valid():
            atdobj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    else:
        at = AttendenceSerializer(atrnum,many=True)
        return Response(at.data,status=HTTP_200_OK)

@api_view(['GET','POST'])
#@login_required(login_url='loginurl')
def att(request):
    at = Attendence.objects.all()
    if request.method == "POST":
        atobj = AttendenceSerializer(data=request.data)
        if atobj.is_valid():
            atobj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    else:
        atdata = AttendenceSerializer(at,many=True)
        return Response(atdata.data,status=HTTP_200_OK)


@api_view(['GET','POST'])
#@login_required(login_url='loginurl')
def insertform(request):
    sdata = Students.objects.all()
    if request.method == "POST":
        s = FormSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST) 
    else:
        std = FormSerializer(sdata,many=True)
        return Response(std.data,status=HTTP_200_OK)          




def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(request,username=uname,password=pwd)
        if user == None:
            return redirect('loginurl')
        else:
            return redirect('selecturl')
    return render(request,'formApp/login.html')


    
'''
 stddata = Students.objects.all()
    if request.method == "POST":
        stdobj = StudentSerializer(data=request.data)
        if stdobj.is_valid():
            stdobj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    else:
        stndobj = StudentSerializer(stddata,many = True)
        return Response(stndobj.data,status=HTTP_200_OK)
'''
         

