from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students,Attendence,Admin

# Create your views here.

'''
def admin(request):
    return HttpResponse('Admin login creataed')

def std(request):
    return HttpResponse('Student Bio Data')

def table(request):
    return render(request,'vsms/table.html')#,{'l':l})
'''


def insert(request):
    if request.method == 'POST':
        stno = request.POST['stdnum']
        stname = request.POST['stdname']
        qlfcn = request.POST['qfn']
        mail = request.POST['email']
        doj = request.POST['doj']
        batch = request.POST['btch'],
        std = Students(stdno = stno,StdName=stname,qualification=qlfcn,DOJ=doj,email = mail,batch=batch)
        std.save()
        return redirect('selecturl')
    return render(request,'vsms/insert.html')

def update(request,stno):
    std = Students.objects.get(stdno=stno)
    if request.method=='POST':
        stno = int(request.POST['stdnum'])
        stname = request.POST['stdname']
        qlfcn = request.POST['qfn']
        mail = request.POST['email']
        doj = request.POST['doj']
        batch = request.POST['btch']
        std = Students(stdno = stno,StdName=stname,qualification=qlfcn,DOJ=doj,email = mail,batch=batch)
        std.save()
        return redirect('selecturl')
    return render(request,'vsms/update.html',{'std':std})

def delete(request,stno):
    std = Students.objects.get(stdno=stno)
    if request.method == 'POST':
        std.delete()
        return redirect('selecturl')
    return render(request,'vsms/delete.html',{'std':std})

def select(request):
    std = Students.objects.all()
    #print(std)
    return render(request,'vsms/select.html',{'std':std})

def stdget(request):
    if request.method == "POST":
        stno = request.POST['stnum']
        s = Students.objects.get(stdno=stno)
        return render(request,'vsms/std.html',{'s':s})
    return render(request,'vsms/stdlogin.html')

'''
def perform(request):
    a = Attendence.objects.all()
    if request.method == "POST":
        rnum = request.POST['rnum']
        s = Students.objects.get(stdno=rnum)
        rno = rnum
        date = request.POST['date']
        ap = request.POST['ap']
        mm = request.POST['mm']
        tm = request.POST['tm']
        d = a.create(date=date,rollnum=rno,attendence = ap,mock=mm,test=tm)
        d.save()
        return HttpResponse('Data Inserted'),redirect('selecturl')
    return render(request,'vsms/Perform.html')#,{'s':s})
    '''

def getatt(request):
    if request.method == "POST":
        rnum = request.POST['rnum']
        s = Students.objects.get(stdno=rnum)
        a = Attendence.objects.filter(rollnum=rnum)
        return render(request,'vsms/stdatt.html',{'a':a,'s':s})
    return render(request,'vsms/getatt.html')

def att(request):
    if request.method == "POST":
        rno = request.POST['rnum']
        atten = request.POST['att']
        mock = request.POST['mock']
        test = request.POST['test']
        date = request.POST['date']
        s = Attendence(rollnum=rno,attendence=atten ,date=date,mock=mock,test=test)
        s.save()
    return render(request,'vsms/attendence.html')



'''       
def stdatt(request):
    if request.method == "POST":
        rnum =request.POST['rnum']
        a = Attendence.objects.filter(rollnum=rnum)
        rno = request.POST['rno']
        att = request.POST['att']
        mck = request.POST['mck']
        tst = request.POST['test']
        dt = request.POST['date']
        k = Attendence(attendence=att,mock=mck,test=tst,rollnum=rno,date=dt)
        k.save()
        return render(request,'vsms/stdatt.html',{'a':a})
'''

'''
def obj(request):

    if request.method == "POST":
        sno = request.POST['stnum']
        s = Students.objects.all()
        l1 = []
        l2 = []
        for rec in s:
            l1.append(rec.StdName)
            l2.append(rec.stdno)
        if sno in l2:
            print(sno)
            return redirect('stdurl',sno)
        else:
            return render(request,'vsms/std.html')
    return render(request,'vsms/stdlogin.html')
'''


