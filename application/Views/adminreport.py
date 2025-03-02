from django.shortcuts import render,redirect
from django.template import loader
import random
from django.http import HttpResponse
from django.contrib import messages

from application.models import AdminClassList
from application.forms import AdminClassListForm

def adminReport(request):
    return render(request,'admin_report.html')