from django.contrib import admin
from .models import MyForm,certificate_form,admin_picture
# Register your models here.

@admin.register(MyForm)
class adminmyform(admin.ModelAdmin):
    list_display=['username','name','is_auth','is_number','std_department','branch_of','phone_no','Address','roll']

@admin.register(certificate_form)
class adminCertificate(admin.ModelAdmin):
    list_display=['certificate_name','std_Fname','std_Lname','std_department','branch_of','rank','marks','std_roll','date']
    
@admin.register(admin_picture)
class adminCertificate(admin.ModelAdmin):
    list_display=['username','admin_profile']
    
