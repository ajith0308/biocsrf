from ctypes import addressof
import email
from django.shortcuts import redirect, render
from requests import session
from .models  import *
from django.contrib import messages
# Create your views here.


def aadher(rep):
    if  rep.method=='POST':
        fname=rep.POST['fname']
        lname=rep.POST['lname']
        dob=rep.POST['dob']
        name=fname+lname
        fathername=rep.POST['Fathername']
        mothername=rep.POST['Mothername']
        address=rep.POST['Address']
        pincode=rep.POST['pincode']
        phone=rep.POST['Phone']
        email=rep.POST['email']
        a= aadher(name=name,dob=dob,fathername=fathername,mothername=mothername,address=address,phone=phone,email=email,pincode=pincode)
        a.save()
        
        return redirect(index)
    else:
         return render(rep,'frontend/aadharmultiform.htm')


        

def arev(request):
    return render(request,'aadherrev.html')

def scr(req):
    return render(req,'frontend/scoller/scollershipform.html')

def  admition(req):
    return render(req,'frontend/admition/admitionforms.html')


def admition_login(req):
    return render(req,'frontend/admition/adformogin.html')

def  admtion_deatile(req):
    return render(req,'frontend/admition/frms.html')

def index(req):
    return render(req,'index.html') 

def  table(req):
    return render(req,'table.html')
    
def profile(req):
    return render(req,'profile.html')
    






