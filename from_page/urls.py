from django.urls import path
from .import views

urlpatterns = [


    path('',views.student,name="student"),
    path('savestudent',views.savestudent,name="savestudent"),
    path('studentlist',views.studentList,name="studentlist"),
    path('editstudent/<int:id>',views.EditStudent,name="editstudent"),
    path('UpdateStudent/<int:id>',views.UpdateStudent,name='UpdateStudent'),
]