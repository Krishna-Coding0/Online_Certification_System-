from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django.contrib.auth.models import Group
from .models import MyForm,certificate_form,admin_picture
from django.contrib.auth.models import User
from .forms import pre_loginform,teacher_crertificate_form,post_signup_form,EditUserprofile,passchange,admin_profile
from .certificate_gentare import cerificate_crate,intoPDF
from .email_varification import accept_student

def home(request):
    return render(request,'student/home.html')

def abouts(request):
    return render(request,'student/abouts.html')

# this View Is Use To Register The New Student 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    # messages.success(request,'Login Successfull')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
            messages.success(request,'You can login Now')
        return render(request, 'student/login.html', {'form':form,"vl":9})
    else:
        return HttpResponseRedirect('/dashboard/')

def pre_loginvalidate(request):
    value=None
    if request.method=="POST":
        form=pre_loginform(request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            lets_check=MyForm.objects.all()
            ad=User.objects.all()
            for i in  lets_check:
                if i.username == un:
                    if i.is_auth:
                        value=1
                        break
                    else:
                        value=2
                        if not i.is_number:
                            return HttpResponseRedirect("/User_signup2/"+un)
            
            for j in  ad:
                if j.username == un:
                    if j.groups.filter(name='Admin').exists():
                        value=1
                        break

            if value==1:
                return HttpResponseRedirect('/login/')
            elif value==2:
                messages.success(request,'You Are On Queue')
                return HttpResponseRedirect("/pre_loginvalidate/")
                 
            else:
                messages.success(request,'Please Sign Up first')
                return HttpResponseRedirect("/signup/")
    else:
        form=pre_loginform()
        return render(request,'student/login.html',{'fm':form,"vl":value})


# signup views
def User_signup(request):
    a=False
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():     
            # Below We Are Taking Two Data Which Whill Be Passed To Accept View 
            un=form.cleaned_data['username']
            fn=form.cleaned_data['first_name']
            em=form.cleaned_data['email']
            reg=MyForm(name=fn,username=un,email=em)
            reg.save()
            user=form.save()
            group=Group.objects.get(name='student')
            user.groups.add(group)
            messages.success(request,'Part 1 Filled Please Enter The Further Details')
            return HttpResponseRedirect("/User_signup2/"+un)
    else:
        form=SignUpForm()
        a=True
    return render(request, 'student/signup.html', {'form':form,'a':a})

def User_signup2(request,uname):    
    if request.method=="POST":
        pi=MyForm.objects.get(username=uname)
        form=post_signup_form(request.POST,request.FILES,instance=pi)
        for i in form:
            print(i)
        if form.is_valid():
            form.save()
            pi=MyForm.objects.get(username=uname)
            # if 2nd login form is not filled By The User then is_number Will Be False
            pi.is_number=True
            pi.save()
            return HttpResponseRedirect('/pre_loginvalidate/')
        else:
            return HttpResponse("Kuch Galt Hai")
    else:
        pi=MyForm.objects.get(username=uname)
        form=post_signup_form(instance=pi)
        return render(request, 'student/signup2.html', {'form':form,"image":pi})



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def dashboard(request):
    if  request.user.is_authenticated:
        current_user=request.user
        if current_user.groups.filter(name='Admin').exists():
            form=MyForm.objects.filter(is_auth=False)
            profile=User.objects.get(username=current_user)
            image=admin_picture.objects.get(username=current_user)
            
            return render(request,'student/dashboard.html',{'profile':profile,'form':form,'image':image})
        else:
            fullname=current_user.get_full_name()
            gps=current_user.groups.all()
            profile=MyForm.objects.get(username=current_user)
            
            return render(request,'student/student_dashboard.html',{'group':gps,'profile':profile})
    else:
        return HttpResponseRedirect('/pre_loginvalidate/')



# this Method is use to render all Request made by Student for login until teacher accept the reqeust student cant login
def accepts(request,uname):
    pi=MyForm.objects.get(username=uname)
    pi.is_auth=True
    pi.save()
    accept_student(pi.email,1,pi.name)
    return HttpResponseRedirect('/dashboard/')


def details(request,uname):
    pi=MyForm.objects.get(username=uname) 
    return render(request,'student/studentdetails.html',{'details':pi})


def rejects(request,uname):
    pi=User.objects.get(username=uname)
    pi2=MyForm.objects.get(username=uname)
    accept_student(pi2.email,0,pi2.name)
    pi2.delete()
    pi.delete()
    return HttpResponseRedirect('/dashboard/')


def add_certificate(request):
    if request.method=="POST":
        pi=teacher_crertificate_form(request.POST)
        if pi.is_valid():
            cn=pi.cleaned_data['certificate_name']
            sfn=pi.cleaned_data['std_Fname']
            sln=pi.cleaned_data['std_Lname']
            sd=pi.cleaned_data['std_department']
            bf=pi.cleaned_data['branch_of']
            rk=pi.cleaned_data['rank']
            mk=pi.cleaned_data['marks']
            rn=pi.cleaned_data['std_roll']
            dt=pi.cleaned_data['date']
            # below Im Call a fuction which is gonna take my default Certificate image and gonna Write Data on certificate 
            # accoring to Details given By The admin
            new_name=cerificate_crate(cn)
            a=f"media/studentcertificate_image/{new_name}"
            intoPDF(a,rn)
            s=certificate_form(certificate_name=cn,std_Fname=sfn,std_Lname=sln,std_department=sd,branch_of=bf,rank=rk,marks=mk,std_roll=rn,date="2022-03-02",adminupload=f"studentcertificate_image/{cn}.png",pdf=f"studentcertificate_PDF/{rn}.pdf")
            s.save()
            messages.success(request,'Certificate Added Successfully !!')
        pi=teacher_crertificate_form() 
    else:
        pi=teacher_crertificate_form()
    return render(request,'student/addnewcertificate.html',{'form':pi})

def show_student_detail(request):
    std_all=certificate_form.objects.all()
    return render(request,'student/show_all_student_certificate.html',{'show':std_all})

# Admin/Teacher Can View All Student Who Are In The Database:
def view_all_register_student(request):
    form=MyForm.objects.all()
    return render(request,'student/showallregiterstudent.html',{'form':form})

def add_falucty(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():    
            user=form.save()
            group=Group.objects.get(name='Admin')
            user.groups.add(group)
            form=SignUpForm()
            return HttpResponseRedirect("/")
    else:
        form=SignUpForm()
        a=False
    return render(request, 'student/signup.html', {'form':form,'a':a})

def show_falucty(request):
    a=[]
    form=User.objects.all()
    # b=request.user.groups.filter(name='Admin').exists()
    for i in form:
        if i.groups.filter(name='Admin').exists():
            a.append(i)
        else:
            pass
        
    return render(request,'student/showalladmin.html', {'form':a})


def show_single_student_detail(request,uname):
    if  request.user.is_authenticated:
        user_detail=MyForm.objects.get(username=uname)
        certificate=certificate_form.objects.get(username=uname)
        # if user_detail==certificate:


def delete_certificate(request,certificatename,rollno):
    if  request.user.is_authenticated:
        d=certificate_form.objects.filter(certificate_name=certificatename,std_roll=rollno)
        d.delete()
        messages.success(request,"Removed Certificate Succesfully!!")

        return HttpResponseRedirect('/show_student_detail/')


def update_certificate(request,certificatename,rollno):
    if  request.user.is_authenticated:
        if request.method=="POST":
            d=certificate_form.objects.get(certificate_name=certificatename,std_roll=rollno)
            pi=teacher_crertificate_form(request.POST,instance=d)
            d.delete()
            if pi.is_valid():
                cn=pi.cleaned_data['certificate_name']
                sfn=pi.cleaned_data['std_Fname']
                sln=pi.cleaned_data['std_Lname']
                sd=pi.cleaned_data['std_department']
                bf=pi.cleaned_data['branch_of']
                rk=pi.cleaned_data['rank']
                mk=pi.cleaned_data['marks']
                rn=pi.cleaned_data['std_roll']
                dt=pi.cleaned_data['date']
                
                new_name=cerificate_crate(cn)
                a=f"media/studentcertificate_image/{new_name}"
                intoPDF(a,rn)
                s=certificate_form(certificate_name=cn,std_Fname=sfn,std_Lname=sln,std_department=sd,branch_of=bf,rank=rk,marks=mk,std_roll=rn,date="2022-03-02",adminupload=f"studentcertificate_image/{cn}.png",pdf=f"studentcertificate_PDF/{rn}.pdf")
                s.save()
                
                return HttpResponseRedirect('/show_student_detail/')
        else:
            d=certificate_form.objects.get(certificate_name=certificatename,std_roll=rollno)
            pi=teacher_crertificate_form(instance=d)
        return render(request,'student/updatecertificate.html',{'form':pi})
    else:
        return HttpResponseRedirect('/dashboard/')

# Admin profile Update 
def profile(request):
    if request.user.groups.filter(name='Admin').exists():
        if  request.user.is_authenticated:
            # a=False
            if request.method=="POST":
                my_form=admin_picture.objects.get(username=request.user)
                form=admin_profile(request.POST,request.FILES,instance=my_form)
                # print(request.POST["username"])
                if form.is_valid():
                    form.save()

                    return HttpResponseRedirect('/profile/')
            else:
                my_form=admin_picture.objects.get(username=request.user)
                form=admin_profile(instance=my_form)
            return render(request,'student/profileupdate.html',{'form':form,'image':my_form,'user':request.user})
        else:
            return HttpResponseRedirect('/login/')
    else:
        if  request.user.is_authenticated:
            if request.method=="POST":
                my_form=MyForm.objects.get(username=request.user)
                form=post_signup_form(request.POST,request.FILES,instance=my_form)
                if form.is_valid():
                    form.save()

                    return HttpResponseRedirect('/profile/')
            else:
                my_form=MyForm.objects.get(username=request.user)
                form=post_signup_form(instance=my_form)
            return render(request,'student/student_profile_update.html',{'form':form,'image':my_form})
        else:
            return HttpResponseRedirect('/login/')
        
        


# when Admin Like To Check One One Student Detail About There Certificate
def check_one_student_all_certificate(request,roll,name):
    if  request.user.is_authenticated:
        my_form=certificate_form.objects.filter(std_roll=roll)
        return render(request,'student/one_student_all_certificate.html',{'form':my_form,'name':name})
    else:
        return HttpResponseRedirect('/login/')


# remove Student Form The Database
def single_std_delete(request,uname):
    if  request.user.is_authenticated:
        pi=User.objects.get(username=uname)
        pi2=MyForm.objects.get(username=uname)
        a=pi2.roll
        pi2.delete()
        pi.delete()
        try:
            pi3=certificate_form.objects.get(std_roll=a)
            pi3.delete()
        except:
            pass

        return HttpResponseRedirect('/view_all_register_student/')
    else:
        return HttpResponseRedirect('/login/')



def user_profile_update(request):
    if request.user.is_authenticated:
        b=True
        if request.method=="POST":
            fm=EditUserprofile(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Your Profile Details Updated ')
                fm.save()
        else:
            fm=EditUserprofile(instance=request.user)
        return render(request,"student/userprofileupdate.html",{'form':fm,'b':'b'})

    else:
        return HttpResponseRedirect('/login/')


def user_change_pass(request):
    if request.user.is_authenticated:
        b=False
        if request.method=="POST":
            fm=passchange(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Your Password Have Changed')
                return HttpResponseRedirect('/dashboard/')
        else:
            fm=passchange(user=request.user)
        return render(request,'student/userprofileupdate.html',{'form':fm,'b':b})
    else:
        return HttpResponseRedirect('/login/')



def searchcertificate(request):
    if request.method=="POST":
        a=request.POST['gsearch']
        ser=certificate_form.objects.filter(std_roll=a)
        return render(request,'student/searchresult.html',{'sr':ser})
    else:
        return HttpResponseRedirect('/dashboard/')


def search_student(request):
    pass