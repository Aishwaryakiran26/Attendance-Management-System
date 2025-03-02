from django.shortcuts import render,redirect
from django.template import loader
import random
from django.http import HttpResponse
from django.contrib import messages

from application.models import AdminClassList
from application.forms import AdminClassListForm



def adminclasshome(request):
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword']
    try:
        classlist = AdminClassList.objects.all()
    except:
        classlist=''
    return render(request,'admin_class_list_show.html',{"ClassDatas":classlist})


def adminclass(request):
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword']
    if request.method == 'POST':
        form = AdminClassListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Classes has assisgned..!')
            return redirect('/adminclass')

    else:
        form = AdminClassListForm()


    return render(request,'admin_class_list.html',{'form':form})


def adminclassedit(request, id):
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword']
    classes = AdminClassList.objects.get(id=id)  
    return render(request,'admin_class_edit.html', {'form':classes})
def adminclassupdate(request,id): 
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword'] 
    classes = AdminClassList.objects.get(id=id)  
    form = AdminClassListForm(request.POST, instance = classes) 
    print(form) 
    if form.is_valid():  
        print('Update')
        form.save()  
        return redirect("/adminclasshome")  
    else:
        print('form is not a valid')
    return render(request, 'admin_class_edit.html', {'form': classes})

def adminclassdelete(request, id): 
    if request.session.has_key('adminpassword'):
        userid = request.session['adminpassword'] 
    classes = AdminClassList.objects.get(id=id)  
    classes.delete()  
    return redirect("/adminclasshome")