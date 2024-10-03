from django.shortcuts import render,redirect
from .forms import StudentForm,CourseForm
from .models import Student,Course
# Create your views here.

# def FormPage(request):
#     return render(request,'formpage.html')

# def Login(request):
#     return render(request,'studentlogin.html')

# def student(request):
#     form = StudentForm
#     return render(request,'student.html',{'f':form})


# # def savestudent(request):
# #     context = {}
# #     s = StudentForm(request.POST)
# #     if(s.is_valid()):
# #         s.save()
# #     context['s'] = s
# #     return render(request,'student.html',context)

# def savestudent(request):
#     if(request.method == 'POST'):
#         s = StudentForm(request.POST)
#         s.save()
#         # return render(request,'student.html',{'form':s})
#         return redirect('studentlist')

# def studentList(request):
#     s = Student.objects.all()
#     return render(request,'studentlist.html',{'f':s})


# def EditStudent(request,id):
#     s = Student.objects.get(pk=id)
#     r = StudentForm(instance=s)
#     return render(request,'editstudent.html',{'f':r,'id':id})

# def UpdateStudent(request,id):
#     a = Student.objects.get(pk=id)
#     form = StudentForm(request.POST,instance=a)
#     if(form.is_valid()):
#         form.save()
#         return render(request,'success.html',{'f':form})
    
# def DeleteStudent(request,id):
#     a = Student.objects.get(pk=id)
#     if(request.method == 'GET'):
#         a.delete()
#         return redirect('studentlist')

def home(request):
    return render(request,'homepage.html')
def course(request):
    form = CourseForm
    return render(request,'CourseForm.html',{'f':form})


def savecourse(request):
    if(request.method == 'POST'):
        s = CourseForm(request.POST)
        s.save()
        return redirect('courselist')
    
def CourseList(request):
    c = Course.objects.all()
    return render(request,'courselist.html',{'f':c})


def EditCourse(request,id):
    s = Course.objects.get(pk=id)
    r = CourseForm(instance=s)
    return render(request,'editcourse.html',{'f':r,'id':id})

def UpdateCourse(request,id):
    a = Course.objects.get(pk=id)
    form = CourseForm(request.POST,instance=a)
    if(form.is_valid()):
        form.save()
        return  redirect('courselist')
    
def DeleteCourse(request,id):
    a = Course.objects.get(pk=id)
    if(request.method == 'GET'):
        a.delete()
        return redirect('courselist')