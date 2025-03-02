from django.contrib import admin
from application.models import AdminRegister,AdminStudent,AdminTeacher,AdminClassList,TakeAttendance,LeaveRequest

admin.site.register(AdminRegister)
admin.site.register(AdminStudent)
admin.site.register(AdminTeacher)
admin.site.register(AdminClassList)
admin.site.register(TakeAttendance)
admin.site.register(LeaveRequest)