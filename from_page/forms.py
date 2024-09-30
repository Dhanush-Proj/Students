from django.db import models
from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'Student_ID',
            'first_name',
            'last_name',
            'age',
            'phone_no',
            'email_id',
        ]