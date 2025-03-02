from django.shortcuts import render,redirect
from django.template import loader
import random
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

from application.models import AdminRegister,AdminStudent,AdminTeacher,TakeAttendance,LeaveRequest
from application.forms import AdminRegisterForm,LoginForm, AdminStudentForm


def studentlogin(request):
    if request.session.has_key('adminstudentregister'):
        userid = request.session['adminstudentregister']
        
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            passwords = request.POST['passwords']
            print(passwords)
            if AdminStudent.objects.filter(adminstudentregister=passwords) and AdminStudent.objects.filter(adminstudentname=username):
                messages.info(request,'Login Successful')
                request.session['adminstudentregister'] = passwords
                messages.info(request,"Login Successfully..!")
                return redirect('/studenthomepage')
            else:
                messages.info(request,'Invalide username or password')

        else:
            print('The form is not a valid')
    else:
        form = LoginForm()

    return render(request,'studentloginpage.html',{'form':form})

def studenthomepage(request):
    if request.session.has_key('adminstudentregister'):
        userid = request.session['adminstudentregister']
        print(userid)
        leave_requests = LeaveRequest.objects.filter(student__adminstudentregister=userid)
        print(leave_requests)
    else:
        leave_requests = []
        
        
    return render(request, 'studenthomepage.html', {'leave_requests': leave_requests})

def studentattendancelist(request):
    if request.method == 'POST':
        if request.session.has_key('adminstudentregister'):
            userid = request.session['adminstudentregister']
            print("#################### Views attendance #################")
            student_id = userid#request.POST['userid']
            sub = request.POST['subject']
            student = AdminStudent.objects.filter(adminstudentregister=student_id)[0]
            subs = AdminTeacher.objects.filter(TeacherId=sub)[0]#.order_by('TeacherSubject').values() 
            print(student,subs.TeacherSubject,'######################################')
            totalattendances = TakeAttendance.objects.filter(student=student.adminstudentregister,
            teacher__TeacherSubject=subs.TeacherSubject)
            #print(totalattendances.student.adminstudentregister)
            context = {'attendance':totalattendances}
            return render(request,'student_attendancelist.html',context)
        else:
            return redirect('/home')
    else:
    
        form = AdminTeacher.objects.filter().order_by('TeacherSubject').values()
    
    return render(request,'student_attendancelist.html',{'form':form})

def studentleave(request):

    return render(request,'studenthomepage.html',{'form':form})
def studentlogout(request):
    username='adminstudentregister' in request.session
    if username==True:
        d=request.session['adminstudentregister']
        del request.session['adminstudentregister']
        messages.info(request,"Logout Successfully")
    else:
        messages.info(request,"Alredy Logout")

    return redirect('/home')
    

