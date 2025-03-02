from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
import random
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

from application.models import AdminRegister,AdminStudent,AdminTeacher,TakeAttendance,LeaveRequest
from application.forms import AdminRegisterForm,LoginForm, AdminStudentForm, LeaveRequestForm,UpdateLeaveRequestForm






def leave_request(request):
    if request.session.has_key('adminstudentregister'):
        userid = request.session['adminstudentregister']
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        student = AdminStudent.objects.get(adminstudentregister=userid)
        subjects = request.POST.getlist('subjects')
        
        if form.is_valid():

            leave_date = form.cleaned_data['dates']
            reason = form.cleaned_data['reason']
            full_day = form.cleaned_data['full_day']
            
            if full_day:
                teachers = AdminTeacher.objects.all()
                for teacher in teachers:
                    LeaveRequest.objects.create(
                        student=student,
                        teacher=teacher,
                        dates=leave_date,
                        reason=reason,
                        full_day=full_day
                    )
            else:
                for subject in subjects:
                    teacher = AdminTeacher.objects.get(TeacherSubject=subject)
                    LeaveRequest.objects.create(
                        student=student,
                        teacher=teacher,
                        dates=leave_date,
                        reason=reason,
                        full_day=full_day
                    )
            return HttpResponse('success_page')  # Redirect to a success page after submission
    else:
        form = LeaveRequestForm()
        teachers = AdminTeacher.objects.all()
    
    
    return render(request, 'student_leaverequest.html', {'form': form, 'teachers': teachers})

def leave_requests_for_teacher(request, teacher_id):
    if request.session.has_key('adminstudentregister'):
        userid = request.session['adminstudentregister']
    teacher = get_object_or_404(AdminTeacher, pk=teacher_id)
    leave_requests = LeaveRequest.objects.filter(teacher=teacher)

    if request.method == 'POST':
        form = UpdateLeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = get_object_or_404(LeaveRequest, pk=request.POST.get('leave_request_id'))
            leave_request.accept = form.cleaned_data['accept']
            leave_request.save()
            return redirect('leave_request_for')
    else:
        form = UpdateLeaveRequestForm()

    return render(request, 'leave_requests_for_teacher.html', {
        'teacher': teacher,
        'leave_requests': leave_requests,
        'form': form
    })
def leave_request_for(request):
    if request.session.has_key('TeacherId'):
        userid = request.session['TeacherId']
    teacher = get_object_or_404(AdminTeacher, pk=userid)
    leave_requests = LeaveRequest.objects.filter(teacher=teacher)
    form = UpdateLeaveRequestForm()
    return render(request, 'leave_requests_for_teacher.html', {
        'teacher': teacher,
        'leave_requests': leave_requests,
        'form': form
    })