from django.shortcuts import render,redirect
from django.template import loader
import random
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from application.models import AdminRegister,AdminTeacher,AdminStudent,TakeAttendance
from application.forms import AdminRegisterForm,LoginForm, AdminTeacherForm,AttendanceForm,AdminStudentForm


def teacherlogin(request):
    if request.session.has_key('TeacherId'):
        userid = request.session['TeacherId']
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            passwords = request.POST['passwords']
            if AdminTeacher.objects.filter(TeacherId=passwords) and AdminTeacher.objects.filter(TeacherName=username):
                request.session['TeacherId'] = passwords
                messages.info(request,'Login Successful')
                return redirect('/teacherhomepage')
            else:
                messages.info(request,'Invalide username or password')

        else:
            print('The form is not a valid')
    else:
        form = LoginForm()
    #else:
        #form = LoginForm() #redirect('/home')
    return render(request,'teacherloginpage.html',{'form':form})

def teacherhomepage(request):
    return render(request,'teacherhomepage.html')

def takeattendance(request):
    if request.session.has_key('TeacherId'):
        userid = request.session['TeacherId']
        if request.method == 'POST':
            teacher = AdminTeacher.objects.get(TeacherId=userid)  # Assuming teacher ID is 2
            attendance_records = []

            for student in AdminStudent.objects.all():
                is_present = f'present_{student.pk}' in request.POST
                attendance_records.append(TakeAttendance(
                    student=student,
                    teacher=teacher,
                    times=datetime.now(),
                    present=is_present
                ))
            
            # Bulk create the attendance records for efficiency
            TakeAttendance.objects.bulk_create(attendance_records)
            return redirect('/teacherhomepage')

           # return HttpResponse('Attendance recorded successfully')
        
        else:
            
            branch = request.GET['Select_class']
            sem = request.GET['Select_sem']
            students = AdminStudent.objects.filter(adminstudentclass = branch , adminstudentsem = sem)
            teacher = AdminTeacher.objects.get(TeacherId=userid)
            current_time = datetime.now()
    else:
        return redirect('/home')

    return render(request, 'teacher_takeattendance.html', {
        'students': students,
        'teacher': teacher,
        'time': current_time

    })

def takeattendances(request):
    global Select_class, Select_sem
    Select_class = AdminStudent.objects.order_by('adminstudentclass').values('adminstudentclass').distinct()
    Select_sem = AdminStudent.objects.order_by('adminstudentsem').values('adminstudentsem').distinct()
    return render(request, 'teacher_takeattendance.html', {
        'Select_class':Select_class, 'Select_sem':Select_sem})

def teacher_takeattendance_report(request):
    
    form = AdminTeacher.objects.filter().order_by('TeacherSubject').values()
    return render(request,'teacher_attendancereport.html',{'form':form}) 

def individual_attendance(request):
    student_id = request.GET['registernumber']
    sub = request.GET['Select_Model']
    student = AdminStudent.objects.filter(adminstudentregister=student_id)[0]
    subs = AdminTeacher.objects.filter(TeacherId=sub)[0]#.order_by('TeacherSubject').values() 
    print(student,subs.TeacherSubject,'######################################')
    totalattendances = TakeAttendance.objects.filter(student=student.adminstudentregister, teacher__TeacherSubject=subs.TeacherSubject)
    presents = TakeAttendance.objects.filter(student=student, teacher__TeacherSubject=subs.TeacherSubject,present=True)
    print(totalattendances)
    print(presents)
    per = (len(presents)/len(totalattendances))*100
    print(per)
    content = {
    'name':student.adminstudentname,
    'Total_attendance':len(totalattendances),
    'presents':len(presents),
    'percentage':per,

    }
    return render(request,'individual_attendance.html',content)

def mass_attendance(request):
    date_str = request.GET.get('date')
    subject_id = request.GET.get('Mass_Select_Model')
    if date_str and subject_id:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        year = date_obj.year
        month = date_obj.month
        teacher = AdminTeacher.objects.get(TeacherId=subject_id)
        totalattendance_records = TakeAttendance.objects.filter(
            teacher=teacher,
            times__year=year,
            times__month=month
            ).select_related('student').order_by('times')

        presenttendance_records= TakeAttendance.objects.filter(
            teacher=teacher,
            times__year=year,
            times__month=month,
            present=True
            ).select_related('student').order_by('times')
        per = (len(presenttendance_records)/len(totalattendance_records))*100
        context = {
            'totalattendance_records': len(totalattendance_records),
            'selected_date': date_obj,
            'selected_subject': teacher.TeacherSubject,
            'present':len(presenttendance_records),
            'percentage':per
        }
    
    return render(request,'individual_attendance.html',context)

def teacherlogout(request):
    username='TeacherId' in request.session
    if username==True:
        d=request.session['TeacherId']
        del request.session['TeacherId']
        messages.info(request,"Logout Successfully")
    else:
        messages.info(request,"Alredy Logout")

    return redirect('/home')

'''def takeattendance(request):
    # this is the working code
    students=''
    teacher=''

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Attendance recorded successfully')
        else:
            print(form)
            print("the form is not valid")
    else:
        students = AdminStudent.objects.all()
        teacher = AdminTeacher.objects.get(TeacherId=2)
        form = AttendanceForm(initial={'teacher': teacher})

    return render(request, 'teacher_takeattendance.html', {
        'form': form,
        'students': students,
        'teacher': teacher,
        'time': datetime.now()
    })'''

'''def takeattendancce(request):
    form = AdminStudent.objects.all()
    return render(request,'teacher_takeattendance.html',{'form':form})
def takeAttendanceDetails(request):
    if request.method == 'POST':
        print(request.POST['options'])
        print("################## Attendance ##################")
    return render(request,'teacher_takeattendance.html')'''

'''
            <tbody>
                {% for attendance in form %}
                {% for attendance1 in form1 %}
                <tr>
                    <td>{{ attendance.adminstudentregister }}</td>
                    <td>{{ attendance.adminstudentname }}</td>
                    <td>{{ attendance.adminstudentclass }}</td>
                    <td>{{ attendance1.TeacherName }}</td>
                    <td>{{ attendance1.TeacherSubject }}</td>
                </tr>
                {% endfor %}
                {% endfor %}
            </tbody>
The above code repeated. So correct it.
'''