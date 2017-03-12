from django.shortcuts import render
from django.template import loader
from .models import *

def index(request):
    # school = School.objects.order_by('name')
    # grade_list = Grade.objects.order_by('teacher')
    # children = Child.objects.order_by('last_name')
    # context = {
    # 'grade_list': grade_list,
    # 'children': children,
    # 'school': school,
    # }
    return render(request, 'CRM/index.html')#, context)

def gallery(request):
    # pictures = Picture.objects.order_by('event')
    return render(request, 'CRM/gallery.html')#, {'pictures': pictures})

def schools(request):
    # schools = School.objects.order_by('name')
    return render(request, 'CRM/schools.html')#, {'schools': schools})

def classes(request):
    # classes = Grade.objects.order_by('school')
    return render(request, 'CRM/classes.html')#, {'classes': classes})

def children(request):
    # children = Child.objects.order_by('first_name')
    return render(request, 'CRM/children.html')#, {'children': children})

def reports(request):
    # children = Child.objects.order_by('last_name')
    return render(request, 'CRM/reports.html')#, {'children': children})

def staff(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/staff.html')#, {'staff': staff})

def attendances(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/attendances.html')#, {'staff': staff})

def contactPerson(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/contactPerson.html')#, {'staff': staff})
