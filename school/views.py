from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import students,teachers,departments
from  .forms import department_form,teacher_form,student_form
from . import forms

# Create your views here.
def login(request):
    return render(request,'school/login.html')


def home(request):
   return render(request,'school/home.html')


def dept(request):
   dep = departments.objects.all().values()
   context={
      'dep':dep
   }
   return render(request,'school/departments.html',context)

def teach(request):
   teach = teachers.objects.all().values()
   context={
      'teachers':teach,
   }
   return render(request,'school/teachers.html',context)

def stud(request):
   stud = students.objects.all().values()
   context={
      'students':stud,
   }
   return render(request,'school/students.html',context)

     
   
def aboutus(request):
   stud = students.objects.all().values()
   teach = teachers.objects.all().values()
   dep = departments.objects.all().values()
   context={
      'students':stud,
      'teachers':teach,
      'dep':dep
   }
   return render(request,'school/aboutus.html',context)



def add_dept(request):

   if request.method =='POST':
      depform = department_form(request.POST)

      if depform.is_valid():
         depform.save()
         return redirect('dept')
   else:
      form1 = forms.department_form()

   return render(request,'school/add_dept.html',{'form':form1})




# def add_teach(request):

#    if request.method =='POST':
#       techform = teacher_form(request.POST,request.FILES)

#       if techform.is_valid():
#          print("qqqqqqqqqqqqqqq")
#          techform.save()
#          return redirect('teach')
#       else:
#             # If form is invalid, pass the submitted data back to the form
#             form1 = forms.teacher_form()
#    else:
#       form1 = forms.teacher_form()

#    teach = teachers.objects.all()
#    print("wwwwwwwwwwwwww")
#    return render(request,'school/add_teacher.html',{'form':form1,'teach':teach})




def add_teach(request):
    if request.method == 'POST':
        techform = teacher_form(request.POST, request.FILES)  # request.FILES is essential
        if techform.is_valid():
            techform.save()
            return redirect('teach')
    else:
        techform = teacher_form()

    teach = teachers.objects.all()
    return render(request, 'school/add_teacher.html', {'form': techform, 'teachers': teach})



def add_stud(request):

   if request.method =='POST':
      techform = student_form(request.POST)

      if techform.is_valid():
         techform.save()
         return redirect('stud')
   else:
      form1 = forms.student_form()

   return render(request,'school/add_student.html',{'form':form1})




