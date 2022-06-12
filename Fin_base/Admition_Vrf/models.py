from cmath import nanj
from ctypes import addressof
import email
from unicodedata import name
import uuid
from email.headerregistry import Address
from operator import mod
from pickle import TRUE
from tkinter.tix import Form
from django.db import models
from django.forms import CharField, IntegerField


class Aadher(models.Model):
    aadher_number=models.IntegerField(auto_created=True,primary_key=True,serialize=TRUE )
    name=models.CharField( max_length=50,null=False)
    dob=models.DateField()
    fathername=models.CharField(max_length=150,null=False)
    mothername=models.CharField(max_length=150,null=False)
    address=models.CharField(max_length=250 ,null=False)
    phone=models.BigIntegerField(null=False)
    pincode=models.CharField(max_length=10,null=False)
    email=models.EmailField(null=False,unique=True)

class aadher_bio(models.Model):
    aadher=models.IntegerField(unique=True)
    biodata1=models.CharField(max_length=500 ,editable=False )
    biodata2=models.CharField(max_length=500,editable=False)
    biodata3=models.CharField(max_length=500,editable=False)
    biodata4=models.CharField(max_length=500,editable=False)
    biodata5=models.CharField(max_length=500,editable=False)

class admission(models.Model):
    Roll=models.IntegerField(primary_key=True)
    aadher_number=models.IntegerField(unique=True)
    dob=models.DateField()
    name=models.CharField(max_length=150)
    email=models.EmailField()
    mother=models.CharField(max_length=150)
    father=models.CharField(max_length=150)
    income=models.IntegerField()
    gender=models.CharField(max_length=100)

class csrf(models.Model):
    sln=models.IntegerField(auto_created=True,null=False)
    Roll=models.IntegerField(null=False)
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    mark3=models.IntegerField()
    mark4=models.IntegerField()
    mark5=models.IntegerField() 
    biodata1=models.CharField(max_length=500 ,editable=False )
    biodata2=models.CharField(max_length=500,editable=False)
    biodata3=models.CharField(max_length=500,editable=False)
    biodata4=models.CharField(max_length=500,editable=False)
    biodata5=models.CharField(max_length=500,editable=False)













# class crf(models.Model):
#     csrt_number=models.ForeignKey(,max_length=100 , on_delete=CASCADE)
#     student_name=models.CharField(max_length=100)
#     mark=models.IntegerField()

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



    