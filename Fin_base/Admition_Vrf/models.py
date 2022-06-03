from cmath import nanj
from ctypes import addressof
import email
from email.headerregistry import Address
from tkinter.tix import Form
from django.db import models
from django.forms import CharField, IntegerField


class aadher(models.Model):
    aadher_number=models.UUIDField(primary_key=True,auto_created=True )
    name=models.CharField( max_length=50,null=False)
    fathername=models.CharField(max_length=150,null=False)
    mothername=models.CharField(max_length=150,null=False)
    address=models.CharField(max_length=250 ,null=False)
    phone=models.BigIntegerField(null=False)
    pincode=models.CharField(max_length=10,null=False)
    email=models.EmailField(null=False,unique=True)

class aadher_bio(models.Model):
    aadher=models.ForeignKey("aadher", on_delete=models.CASCADE)
    biodata=models.CharField(max_length=95000 ,null=False,editable=False,unique=True)





# class crf(models.Model):
#     csrt_number=models.ForeignKey(,max_length=100 , on_delete=CASCADE)
#     student_name=models.CharField(max_length=100)
#     mark=models.IntegerField()

class  company_api(models.Model):
    username=models.CharField( max_length=50,primary_key=True)
    biodata=models.JSONField()

class student_database(Form):
    name=models.CharField( max_length=50)
    aadher_number=models.IntegerField(null=False,primary_key=True)
    father_name=models.CharField(max_length=50)
    tenth_mark=models.IntegerField()
    plus2_mark=models.IntegerField()
    deplmo_mark=models.IntegerField()
    deg_mark=models.IntegerField()
    msdeg_mark=models.IntegerField()
    phd_mark=models.IntegerField()
    Address=models.CharField(max_length=500)
    phone=models.IntegerField()
    father_income=models.IntegerField()



    