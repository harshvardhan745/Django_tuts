from dataclasses import fields

from django.forms import forms
from django import forms
from mypro1.models import Employee

'''class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '_all_'
'''


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        #fields = ('first_name','email','')

    def clean(self):
        super(EmployeeForm, self).clean()

        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')

        if len(name) < 3:
            self._errors['name'] = self.error_class(
                ['A min of 3 chars required for name'])

        if len(phone) < 11:
            self._errors['phone'] = self.error_class(
                ['A min of 10 values required for phone no'])

        return self.cleaned_data

class EmployeeForm2(forms.Form):
    first_name = forms.CharField(
        label="Enter first name", max_length=50, required=True)
    last_name = forms.CharField(
        label="Enter last name", max_length=10, required=True)
    email = forms.EmailField(label="Enter Email", required=False)
    profile_image = forms.FileField(required=False)  # for creating file input