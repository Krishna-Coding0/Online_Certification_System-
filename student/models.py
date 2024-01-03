import email
from django.db import models
from django.contrib.auth.models import User


class MyForm(models.Model):
    is_auth = models.BooleanField(default=False)
    is_number=models.BooleanField(default=False)
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=50)  
    std_department=models.CharField(max_length=100)
    branch_of=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=13)
    Address=models.CharField(max_length=150)
    roll=models.CharField(max_length=8)
    profile_photo=models.FileField(default='profile_admin/Upload image.png',upload_to='profile_admin')
    


class certificate_form(models.Model):
    certificate_name=models.CharField(max_length=100)
    std_Fname=models.CharField(max_length=40)
    std_Lname=models.CharField(max_length=40)
    std_department=models.CharField(max_length=100)
    branch_of=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    marks=models.CharField(max_length=50)
    std_roll=models.CharField(max_length=8)
    date=models.DateField()
    adminupload=models.FileField(upload_to='studentcertificate_image')
    pdf=models.FileField(upload_to='studentcertificate_PDF')


class admin_picture(models.Model):
    username=models.CharField(max_length=100)
    admin_profile=models.FileField(default='profile_admin/Upload image.png',upload_to='profile_admin')
