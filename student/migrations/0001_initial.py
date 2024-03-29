# Generated by Django 4.1.6 on 2023-02-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('admin_profile', models.FileField(default='profile_admin/Upload image.png', upload_to='profile_admin')),
            ],
        ),
        migrations.CreateModel(
            name='certificate_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=100)),
                ('std_Fname', models.CharField(max_length=40)),
                ('std_Lname', models.CharField(max_length=40)),
                ('std_department', models.CharField(max_length=100)),
                ('branch_of', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('marks', models.CharField(max_length=50)),
                ('std_roll', models.CharField(max_length=8)),
                ('date', models.DateField()),
                ('adminupload', models.FileField(upload_to='studentcertificate_image')),
                ('pdf', models.FileField(upload_to='studentcertificate_PDF')),
            ],
        ),
        migrations.CreateModel(
            name='MyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_auth', models.BooleanField(default=False)),
                ('is_number', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=50)),
                ('std_department', models.CharField(max_length=100)),
                ('branch_of', models.CharField(max_length=10)),
                ('phone_no', models.CharField(max_length=13)),
                ('Address', models.CharField(max_length=150)),
                ('roll', models.CharField(max_length=8)),
                ('profile_photo', models.FileField(default='profile_admin/Upload image.png', upload_to='profile_admin')),
            ],
        ),
    ]
