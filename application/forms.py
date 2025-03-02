from django import forms
from captcha.fields import ReCaptchaField 
from captcha.widgets import ReCaptchaV2Checkbox
from application.models import AdminRegister,AdminStudent,AdminTeacher,AdminClassList,TakeAttendance,LeaveRequest



class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model = AdminRegister
        fields = "__all__"

class LoginForm(forms.Form): 
    username = forms.CharField(max_length=20) 
    passwords = forms.CharField(max_length=20) 
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 

class AdminStudentForm(forms.ModelForm):
    class Meta:
        model = AdminStudent
        fields = "__all__"

class AdminTeacherForm(forms.ModelForm):
    class Meta:
        model = AdminTeacher
        fields = "__all__"

class AdminClassListForm(forms.ModelForm):
    class Meta:
        model = AdminClassList
        fields = "__all__"  

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = TakeAttendance
        fields = ['student', 'teacher', 'present']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['dates', 'reason', 'full_day']
        widgets = {
            'dates': forms.DateInput(attrs={'type': 'dates'}),
            'reason': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter the reason for your leave...'}),
        }

class UpdateLeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['accept']

class TakesAttendanceForm(forms.ModelForm):
    class Meta:
        model = TakeAttendance
        fields = ['student']
 




