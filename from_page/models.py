from django.db import models

# Create your models here.


class Student(models.Model):
    Student_ID = models.IntegerField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    phone_no = models.IntegerField()     
    email_id = models.EmailField()

    def __str__(self):
        return self.first_name+self.last_name 