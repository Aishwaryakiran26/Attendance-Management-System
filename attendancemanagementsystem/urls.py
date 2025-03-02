"""collegemanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application.Views import admin_student,admin_teacher,admin_classlist,adminreport,students,teachers,leave
from application import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home',views.home, name = 'home'),

    #path('studentlogin',views.studentlogin,name='studentlogin'),
    #*************** Admin Student *************************
    path('adminhome',admin_student.adminhome,name='adminhome'),
    path('admin_register',admin_student.admin_register,name='admin_register'),
    path('adminlogin',admin_student.adminlogin,name='adminlogin'),
    path('adminstudent',admin_student.adminstudent,name='adminstudent'),
    path('adminstudentedit/<int:id>',admin_student.adminstudentedit),
    path('adminstudentupdate/<int:id>',admin_student.adminstudentupdate),
    path('adminstudentdelete/<int:id>',admin_student.adminstudentdelete),
    path('adminstudentsearch',admin_student.adminstudentsearch, name='adminstudentsearch'),

    #************** Admin Teacher *************************
    path('adminteacher',admin_teacher.adminteacher,name='adminteacher'),
    path('adminteacheredit/<int:id>',admin_teacher.adminteacheredit),
    path('adminteacherupdate/<int:id>',admin_teacher.adminteacherupdate),
    path('adminteacherdelete/<int:id>',admin_teacher.adminteacherdelete),
    path('adminteachersearch',admin_teacher.adminteachersearch, name='adminteachersearch'),

    #************ Admin Class List ************************
    path('adminclasshome',admin_classlist.adminclasshome,name='adminclasshome'),
    path('adminclass',admin_classlist.adminclass,name='adminclass'),
    path('adminclassedit/<int:id>',admin_classlist.adminclassedit),
    path('adminclassupdate/<int:id>',admin_classlist.adminclassupdate),
    path('adminclassdelete/<int:id>',admin_classlist.adminclassdelete),
    path('adminReport',adminreport.adminReport,name='adminReport'),
    path('adminlogout',admin_student.adminlogout,name='adminlogout'),


    #****************** Students *********************************
    path('studentlogin',students.studentlogin,name='studentlogin'),
    path('studenthomepage',students.studenthomepage,name='studenthomepage'),
    path('studentattendancelist',students.studentattendancelist,name='studentattendancelist'),
    path('studentleave',students.studentleave,name='studentleave'),
    path('studentlogout',students.studentlogout,name='studentlogout'),




    #****************** Teachers *********************************
    path('teacherlogin',teachers.teacherlogin,name='teacherlogin'),
    path('teacherhomepage',teachers.teacherhomepage,name='teacherhomepage'),
    #path('takeattendancce',teachers.takeattendancce,name='takeattendancce'),
    #path('takeAttendanceDetails',teachers.takeAttendanceDetails,name='takeAttendanceDetails'),
    path('takeattendance',teachers.takeattendance,name='takeattendance'),
    path('takeattendances',teachers.takeattendances,name='takeattendances'),
    path('teacher_takeattendance_report',teachers.teacher_takeattendance_report,name='teacher_takeattendance_report'),
    path('teacher_takeattendance_report',teachers.teacher_takeattendance_report,name='teacher_takeattendance_report'),
    path('individual_attendance',teachers.individual_attendance,name='individual_attendance'),
    path('mass_attendance',teachers.mass_attendance,name='mass_attendance'),
    path('teacherlogout',teachers.teacherlogout,name='teacherlogout'),

    #******************* Leave Request *****************************
    path('leave_request',leave.leave_request,name='leave_request'),
    path('leave_request_for',leave.leave_request_for,name='leave_request_for'),
    path('leave_requests_for_teacher/<int:teacher_id>', leave.leave_requests_for_teacher),
    #path('leave_requests_for_teacher/<int:teacher_id>/',leave.leave_requests_for_teacher),

    
]
