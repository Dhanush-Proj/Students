from django.db import models

# Create your models here.


class Student(models.Model):
    Student_ID = models.IntegerField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    phone_no = models.IntegerField()     
    email_id = models.EmailField(null=True)

    def __str__(self):
        return self.first_name+self.last_name 
    

class Course(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)
    course_fees = models.FloatField()
    course_duration = models.DurationField(max_length=6)


    def __str__(self):
        return self.course_name