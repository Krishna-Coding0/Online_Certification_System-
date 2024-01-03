"""certificate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('abouts/',views.abouts,name="abouts"),
    path('login/', views.user_login,name="login"),
    path('signup/', views.User_signup,name="signup"),
    path('logout/', views.user_logout,name="logout"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('check_one_student_all_certificate/<str:roll>/<str:name>/', views.check_one_student_all_certificate,name="check_one_student_all_certificate"),
    path('accepts/<str:uname>/', views.accepts,name="accept"),
    path('pre_loginvalidate/', views.pre_loginvalidate,name="pre_loginvalidate"),
    path('details/<str:uname>/', views.details,name="details"),
    path('rejects/<str:uname>/', views.rejects,name="rejects"),
    path('add_certificate/', views.add_certificate,name="add_certificate"),
    path('show_student_detail/', views.show_student_detail,name="show_student_detail"),
    path('User_signup2/<str:uname>/', views.User_signup2,name="User_signup2"),
    path('view_all_register_student/', views.view_all_register_student,name="view_all_register_student"),
    path('add_falucty/', views.add_falucty,name="add_falucty"),
    path('show_falucty/', views.show_falucty,name="show_falucty"),
    path('delete_certificate/<str:certificatename>/<str:rollno>', views.delete_certificate,name="delete_certificate"),
    path('update_certificate/<str:certificatename>/<str:rollno>', views.update_certificate,name="update_certificate"),
    path('profile/', views.profile,name="profile"),
    path('single_std_delete/<str:uname>/', views.single_std_delete,name="single_std_delete"),
    path('user_profile_update/', views.user_profile_update,name="user_profile_update"),
    path('user_change_pass/', views.user_change_pass,name="user_change_pass"),
    path('searchcertificate/', views.searchcertificate,name="searchcertificate"),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

