# Create your models here.
from django.db import models


'''class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    roll_no = models.IntegerField(blank=True)

    class Meta:
        db_table = "student"
'''

class Employee(models.Model):
    name = models.CharField(max_length=130, default='')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10, default='')

    class Meta:
        db_table = "employee"

# python3 manage.py makemigrations
# python3 manage.py migrate

class EmployeePimg(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)

    profile_image = models.FileField(blank=True)

    class Meta:
        db_table = "employee_pimg"