from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.

def FormPage(request):
    return render(request,'formpage.html')

def Login(request):
    return render(request,'studentlogin.html')

def student(request):
    form = StudentForm
    return render(request,'student.html',{'f':form})


# def savestudent(request):
#     context = {}
#     s = StudentForm(request.POST)
#     if(s.is_valid()):
#         s.save()
#     context['s'] = s
#     return render(request,'student.html',context)

def savestudent(request):
    if(request.method == 'POST'):
        s = StudentForm(request.POST)
        s.save()
        # return render(request,'student.html',{'form':s})
        return redirect('studentlist')

def studentList(request):
    s = Student.objects.all()
    return render(request,'studentlist.html',{'f':s})


def EditStudent(request,id):
    s = Student.objects.get(pk=id)
    r = StudentForm(instance=s)
    return render(request,'editstudent.html',{'f':r,'id':id})

def UpdateStudent(request,id):
    a = Student.objects.get(pk=id)
    form = StudentForm(request.POST,instance=a)
    if(form.is_valid()):
        form.save()
        return render(request,'success.html',{'f':form})
    
