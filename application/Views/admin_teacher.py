from django.shortcuts import render,redirect
from django.template import loader
import random
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

from application.models import AdminTeacher
from application.forms import AdminTeacherForm

def adminteacher(request):
    if request.method == 'POST':
        form = AdminTeacherForm(request.POST)
        admin_teacher_id = request.POST['TeacherId']
        if AdminTeacher.objects.filter(TeacherId=admin_teacher_id):
            messages.info(request,'The Teacher ID alredy Exist.')
            return redirect('/adminteacher')
        else:
            if form.is_valid():

                form.save()
                messages.info(request,'Teacher info saved..!')
                return redirect('/adminteacher')

    else:
        form = AdminTeacherForm()
    try:
        teacherlist = AdminTeacher.objects.all()
    except:
        teacherlist=''

    return render(request,'admin_teacher.html',{'form':form,"TeacherDatas":teacherlist})
def adminteacheredit(request, id):
    teacher = AdminTeacher.objects.get(TeacherId=id)  
    return render(request,'admin_teacher_edit.html', {'form':teacher})
def adminteacherupdate(request,id):  
    teacher = AdminTeacher.objects.get(TeacherId=id)  
    form = AdminTeacherForm(request.POST, instance = teacher)  
    if form.is_valid():  
        form.save()  
        return redirect("/adminteacher")  
    return render(request, 'admin_teacher_edit.html', {'form': teacher})

def adminteacherdelete(request, id):  
    teacher = AdminTeacher.objects.get(TeacherId=id)  
    teacher.delete()  
    return redirect("/adminteacher") 

def adminteachersearch(request):
    if request.method == 'POST':
        ids = request.POST['search']
        print(ids)
        teachersearch = AdminTeacher.objects.filter(TeacherId=ids)
        print('################################')
        print(teachersearch)
        #return redirect('/adminstudent')
        return render(request, 'admin_teacher.html', {'TeacherDatas': teachersearch,'all':1})
    return render(request, 'admin_teacher.html', {'TeacherDatas': teachersearch})
    
