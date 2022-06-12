from ctypes import addressof
import email
import profile
from django.contrib import messages
from re import A
from django.shortcuts import redirect, render
from matplotlib.pyplot import table
from numpy import number
from requests import request, session
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
# Create your views here.
#aadhar regeristration
def aadher(rep):
    if  rep.method=='POST':
        fname=rep.POST['fname']
        lname=rep.POST['lname']
        dob1=rep.POST['dob']
        name1=fname+lname
        fathername1=rep.POST['Fathername']
        mothername1=rep.POST['Mothername']
        address1=rep.POST['Address']
        pincode1=rep.POST['pincode']
        phone1=rep.POST['Phone']
        email1=rep.POST['email']
        fg1=rep.POST['imgFinger1']
        fg2=rep.POST["imgFinger2"]
        fg3=rep.POST["imgFinger3"]
        fg4=rep.POST["imgFinger4"]
        fg5=rep.POST["imgFinger5"]
        if Aadher.objects.filter(email=email).exists():
                messages.info(rep, 'Email taken')
                return render(rep,'aadhar/aadharmultiform.htm')
        else:
            a=Aadher(name=name1,dob=dob1,fathername=fathername1,mothername=mothername1,address=address1,phone=phone1,pincode=pincode1,email=email1)
            a.save()
            dp=Aadher.objects.filter(email=email1)
            a=dp[0]. aadher_number
            b=aadher_bio(aadher=a,biodata5=fg5,biodata4=fg4,biodata3=fg3,biodata2=fg2,biodata1=fg1)
            b.save()
            messages.info(rep, 'created success')
            return render(rep,'aadhar/aadharmultiform.htm')
    else:
         return render(rep,'aadhar/aadharmultiform.htm')


def verifyandStore(request):
 
            a1=request.session.get('name')
            a2 =   request.session.get('dob')
            a3 =  request.session.get('email')
            a4=   request.session.get('fname')
            a5=   request.session.get('aadher')
            a6=   request.session.get('gender')
            a7= request.session.get('mother')
            a8= request.session.get('income')
            a=admission(aadher_number=a5,dob=a2,name=a1,email=a3,mother=a7,father=a4,income=a8,gender=a6)
            a.save()
            return redirect()
               
def getcsrf(request):
    
    if request.method=='POST' :
        id=request.session.get('aadher')
        b=aadher_bio.objects.filter(aadher=id)
        if len(b)>0:
            f1=b[0].biodata1
            f2=b[0].biodata2
            f3=b[0].biodata3
            f4=b[0].biodata4
            f5=b[0].biodata5

            f =[]
    
            contaxt={
                'b1':f1,
                'b2':f2,
                'b3':f3,
                'b4':f4,
                'b5':f5,
               
                        } 
            return render(request,'frontend/admition/verificationsupport.htm',contaxt)
        else:
            #con={ 'aadhar':id,}
            return render(request,'frontend/admition/aadherreg.htm' )
    else:
         id=request.session.get('aadher')
         print(id)
         con={ 'aadhar':id,}
         return render(request,'frontend/admition/aadherreg.htm' ,con)


def srccsrf(request):
    if request.method=='POST' :
         aadher=request.POST['aadhar']
         request.session['aadher']=aadher
         return redirect(srcaadvrf)
    return render(request,'frontend/scoller/scrcsrf.html')

def srcaadvrf(request):
    if request.method == 'POST':
        return redirect(src10csrf)
    else:
         id=request.session.get('aadher')
         b=aadher_bio.objects.filter(aadher=id)
         if len(b)>0:
            f1=b[0].biodata1
            f2=b[0].biodata2
            f3=b[0].biodata3
            f4=b[0].biodata4
            f5=b[0].biodata5    
            contaxt={
                'b1':f1,
                'b2':f2,
                'b3':f3,
                'b4':f4,
                'b5':f5,
               
                        } 
            

    return render(request,'frontend/scoller/verfication.html',contaxt)

def src10csrf(request):
    if request.method=='POST' :
        x=request.POST['ten']
        request.session['ten']=x
        return redirect(scr10vrf)
    return render(request,'frontend/scoller/scrcsrf10.html')

def scr10vrf(request):
    if request.method=='POST' :
         return redirect(src12csrf)
    else:
         id=request.session.get('ten')
         b=aadher_bio.objects.filter(aadher=id)
         if len(b)>0:
            f1=b[0].biodata1
            f2=b[0].biodata2
            f3=b[0].biodata3
            f4=b[0].biodata4
            f5=b[0].biodata5    
            contaxt={
                'b1':f1,
                'b2':f2,
                'b3':f3,
                'b4':f4,
                'b5':f5,
               
                        } 
    return render(request,'frontend/scoller/verfication10.html',contaxt)
  
def src12csrf(request):
    if request.method=='POST' :
        aadher=request.POST['t2']
        request.session['t2']=aadher
        return redirect(scr12vrf)
    return render(request,'frontend/scoller/scrcsrf12.html')
    
def scr12vrf(request):
    id=request.session.get('t2')
    b=aadher_bio.objects.filter(aadher=id)
    if len(b)>0:
            f1=b[0].biodata1
            f2=b[0].biodata2
            f3=b[0].biodata3
            f4=b[0].biodata4
            f5=b[0].biodata5    
            contaxt={
                'b1':f1,
                'b2':f2,
                'b3':f3,
                'b4':f4,
                'b5':f5,
               
                        }  
            return render(request,'frontend/scoller/verfication12.html',contaxt)
    

def scrapply(req):

    return render(req,'frontend/scoller/table.html')


def scr(req):
    if req.method == 'POST':
        USER=   req.POST['roolnumber']
        password= req.POST['password']
        user = auth.authenticate(username=USER, password=password)
        # print(auth.objects.filter(is_superuser=1))
        if user is  None:
            #auth.login(req, user)
           # req.session["uid"] = user
            req.session['id'] = user
            return redirect(scrapply)
    return render(req,'frontend/scoller/scrlogin.html')

def  admition(req):
    return render(req,'frontend/admition/admitionforms.html')


def admition_login(req):
    if req.method=='POST':
        Usr=req.POST['email']
        password=req.POST['password']
        user=auth.authenticate(username=Usr,password=password)
        if user is not None:
            #request.session['id']=Usr
            return redirect(profile)
    return render(req,'frontend/admition/adformogin.html')

def  admtion_deatile(req):
    if req.method == 'POST':
        name=req.POST['name']
        dob=req.POST['dob']
        email=req.POST['email']
        aadher=req.POST['aadhar']
        gender=req.POST['gender']
        fname=req.POST['fname']
        mothername=req.POST['mother']
        income=req.POST['income']
        req.session['name']=name
        req.session['dob']=dob
        req.session['email']=email
        req.session['fname']=fname
        req.session['aadher']=aadher
        req.session['gender']=gender
        req.session['mother']=mothername
        req.session['income']=income
        if Aadher.objects.filter( aadher_number=aadher).exists():
            #a=admission(aadher_number=aadher,dob=dob,name=name,email=email,mother=mothername,father=fname,income=income,gender=gender)
            #a.save()
           
            return redirect(getcsrf)
        else:
            return render(req,)


    return render(req,'frontend/admition/newstudentreg.html')


def index(req):
    return render(req,'index.html') 

def  table(req):

    return render(req,'table.html')
    
def profile(req):
    if req.method == 'POST':
        p1=req.POST['fpass']
        p2=req.POST['lpass']
        email=req.POST['email']
        if p1==p2:
            User.objects.create(username=email,password=p1)
        else :
            messages.info("Password mismatch") 
            return render(req,'profile.html',context)
    else:
     email=req.session.get('email')
     context={
        "email":email,

     }
     return render(req,'profile.html',context)
    
def scrdetails(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        email=request.POST['email']
        gender=request.POST['gender']
        fname=request.POST['fname']
        mothername=request.POST['mother']
        income=request.POST['income']
        request.session['name']=name
        request.session['dob']=dob
        request.session['email']=email
        request.session['fname']=fname
        request.session['gender']=gender
        request.session['mother']=mothername
        request.session['income']=income    
        return redirect(srccsrf)
    return render(request,'frontend/scoller/scrdetails.html')

def sucess(request):
        return render(request,"suc.html")



