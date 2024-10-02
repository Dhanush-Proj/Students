from django.db import models
from django.forms import ModelForm
from .models import Student
from .models import Course

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

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_id',
            'course_name',
            'course_fees',
            'course_duration',
        ]