from django.db import models
from datetime import date

class AdminRegister(models.Model):
    adminusername = models.CharField(max_length=20)
    adminemail = models.EmailField()
    adminpassword = models.CharField(max_length=20)

    def __str__(self):
        return '%s'%self.adminusername

class AdminStudent(models.Model):
    adminstudentregister = models.IntegerField(primary_key=True)
    adminstudentname = models.CharField(max_length=20)
    adminstudentclass = models.CharField(max_length=20)
    adminstudentsem = models.IntegerField()

    def __str__(self):
        return '%s'%self.adminstudentregister

class AdminTeacher(models.Model):
    TeacherId = models.IntegerField(primary_key=True)
    TeacherName = models.CharField(max_length=20)
    TeacherSubject = models.CharField(max_length=20)
    def __str__(self):
        return '%s %s %s'%(self.TeacherId, self.TeacherName,self.TeacherSubject)

class AdminClassList(models.Model):
    className = models.CharField(max_length=20)
    classTeacher = models.OneToOneField(AdminTeacher, on_delete=models.CASCADE,default='Teacher Name')
    classRoom = models.CharField(max_length=20)
    class Meta:
        ordering =['classTeacher']
        verbose_name="Class Teacher List"

class TakeAttendance(models.Model):
    student = models.ForeignKey(AdminStudent, on_delete=models.CASCADE)
    teacher = models.ForeignKey(AdminTeacher, on_delete=models.CASCADE)
    times = models.DateTimeField(null=True, blank=True, default=None)
    present = models.BooleanField()


    def __str__(self):
        return '%s '%(self.student)



class LeaveRequest(models.Model):
    student = models.ForeignKey(AdminStudent, on_delete=models.CASCADE)
    teacher = models.ForeignKey(AdminTeacher, on_delete=models.CASCADE)
    reason = models.TextField()
    dates = models.DateField(default=date.today)
    full_day = models.BooleanField()
    accept = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.adminstudentregister} - {self.teacher.TeacherId}'











