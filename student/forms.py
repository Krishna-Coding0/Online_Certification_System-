from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import MyForm, certificate_form,admin_picture



class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Enter Password'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Enter Password Again'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={'first_name':'First Name :','last_name :':'Last Name :','email':'Email :'}
        widgets={'username':forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Username'}),
                'first_name':forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Name'}),
                 'last_name':forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Surname'}),
                 'email':forms.EmailInput(attrs={"class":"form-control",'placeholder':'Enter Email'})
        }
        def clean_up(self):
            var=self.cleaned_data.get('username')
            print("hello",var)





class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,"class":"form-control"}))
    password=UsernameField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password',"class":"form-control"}))



class teacher_crertificate_form(forms.ModelForm):
    class Meta:
        model=certificate_form
        fields=['certificate_name','std_Fname','std_Lname','std_department','branch_of','rank','marks','std_roll','date']
        label={'certificate_name':'Event Name:','std_Fname :':'First Name :','std_Lname':'Last Name :'}
        widgets={'certificate_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Certificate Name'}),
                'std_Fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Name'}),
                 'std_Lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Surname'}),
                 'std_department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Department'}),
                 'branch_of':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Branch (Year)'}),
                 'rank':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Rank'}),
                 'marks':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Marks'}),
                 'std_roll':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Roll No: e.g 19BCA39'}),
                 'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter  Date Of Event Occur'}),
                }


class certificate(forms.Form):
    subject=forms.CharField()
    name=forms.CharField()


class pre_loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Your Username',}))
    
class post_signup_form(forms.ModelForm):
    class Meta:
        model=MyForm
        fields=['username','name','email','std_department','branch_of','phone_no','Address','roll','profile_photo']
        label={'username':'Username :','name':'Name','email':'Email','std_department':'Department :','branch_of':'Branch of (Year) :','phone_no':'Contact No. :','Address':'Address :','roll':'Roll:'}
        help_text={"fname":'100 characters max'}   
        widgets={
                 'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}),
                 'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
                 'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
                 'std_department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Department'}),
                 'branch_of':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Branch'}),
                 'phone_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Phone No.'}),
                 'Address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}),
                 'roll':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Roll No'}),
                 'profile_photo':forms.FileInput(attrs={'class':'form-control'}),
        }
class EditUserprofile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={'first_name':'Name','last_name':'Surname','email' :'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
        }
class passchange(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True,'class':'form-control'}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )

class admin_profile(forms.ModelForm):
    class Meta:
        model=admin_picture
        fields={'username','admin_profile'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'admin_profile':forms.FileInput(attrs={'class':'form-control'}),
        }