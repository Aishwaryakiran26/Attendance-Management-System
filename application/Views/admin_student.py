from django.shortcuts import render,redirect
from django.template import loader
import random
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

from application.models import AdminRegister,AdminStudent
from application.forms import AdminRegisterForm,LoginForm, AdminStudentForm

def home(request):
    return render(request,'mainloginpg.html')

#***************************** Admin Student Records ******************************
def admin_register(request):
    if request.method =='POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['adminusername']
            email = request.POST['adminemail']
            passwords = request.POST['adminpassword']

            
            if AdminRegister.objects.filter(adminusername=username) and AdminRegister.objects.filter(adminemail=email):
                messages.info(request,'Account Exist')
                return redirect('/adminlogin')
            else:
                #passwd=make_password(passwords)
                user=AdminRegister(adminusername=username, adminemail=email,adminpassword=str(passwords))
                user.save()
                messages.info(request,"Register succesfully")
                #return HttpResponse('SignUp Successful')
                return redirect('/adminlogin')
                
        else:
            return HttpResponse('SignUp Fail')
    else:
        form = AdminRegisterForm()
    return render(request,'adminregiter.html',{'form':form})
def adminlogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = request.POST['username']
            passwords = request.POST['passwords']
            if AdminRegister.objects.filter(adminusername=username) and AdminRegister.objects.filter(adminpassword=passwords):
                request.session['adminpassword'] = passwords
                messages.info(request,'Login Successful')
                return redirect('/adminhome')
            else:
                messages.info(request,'Invalide username or password')

        else:
            print('The form is not a valid')
    else:
        form = LoginForm()
    return render(request,'adminloginpage.html',{'form':form})

def adminhome(request):
    return render(request,'adminhomepage.html')
def adminstudent(request):

    if request.method == 'POST':
        if request.session.has_key('adminpassword'):
            userid = request.session['adminpassword']
        form = AdminStudentForm(request.POST)
        admin_stu_reg_no = request.POST['adminstudentregister']
        if AdminStudent.objects.filter(adminstudentregister=admin_stu_reg_no):
            messages.info(request,'The student register number alredy Exist.')
            return redirect('/adminstudent')
        else:
            if form.is_valid():

                form.save()
                messages.info(request,'Student info saved..!')
                return redirect('/adminstudent')

    else:
        form = AdminStudentForm()
    studentlist = AdminStudent.objects.all()

    return render(request,'admin_students.html',{'form':form,"StudentDatas":studentlist})
def adminstudentedit(request, id):
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword']
    student = AdminStudent.objects.get(adminstudentregister=id)  
    return render(request,'admin_student_edit.html', {'form':student})
def adminstudentupdate(request,id):
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword']
    student = AdminStudent.objects.get(adminstudentregister=id)  
    form = AdminStudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/adminstudent")  
    return render(request, 'admin_student_edit.html', {'form': student})  

def adminstudentdelete(request, id):  
    student = AdminStudent.objects.get(adminstudentregister=id)  
    student.delete()  
    return redirect("/adminstudent") 
def adminstudentsearch(request):
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword']
    if request.method == 'POST':
        ids = request.POST['search']
        studentsearch = AdminStudent.objects.filter(adminstudentregister=ids)
        print('################################')
        print(studentsearch)
        #return redirect('/adminstudent')
        return render(request, 'admin_students.html', {'StudentDatas': studentsearch,'all':1})
    return render(request, 'admin_students.html', {'studentsearch': studentsearch})
    


def adminlogout(request):
    username='adminpassword' in request.session
    if username==True:
        d=request.session['adminpassword']
        del request.session['adminpassword']
        messages.info(request,"Logout Successfully")
    else:
        messages.info(request,"Alredy Logout")

    return redirect('/home')