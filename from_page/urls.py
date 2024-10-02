from django.urls import path
from .import views

urlpatterns = [


    # path('',views.student,name="student"),
    # path('savestudent',views.savestudent,name="savestudent"),
    # path('studentlist',views.studentList,name="studentlist"),
    # path('editstudent/<int:id>',views.EditStudent,name="editstudent"),
    # path('UpdateStudent/<int:id>',views.UpdateStudent,name='UpdateStudent'),
    # path('DeleteStudent/<int:id>',views.DeleteStudent,name="DeleteStudent"),

    path('',views.course,name="course"),
    path('courselist',views.CourseList,name="courselist"),
    path('savecourse',views.savecourse,name="savecourse"),
    path('editcourse/<int:id>',views.EditCourse,name="editcourse"),
    path('updatecourse/<int:id>',views.UpdateCourse,name="updatecourse"),
    path('deletecourse/<int:id>',views.DeleteCourse,name="deletecourse"),
]