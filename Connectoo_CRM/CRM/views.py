from django.shortcuts import render
from django.template import loader
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def index(request):
    school = KGardens.objects.order_by('name')
    group = Groups.objects.order_by('name')
    children = Kids.objects.order_by('last_name')
    context = {
    'group': group,
    'children': children,
    'school': school,
    }
    return render(request, 'CRM/index.html', context)

def schools_table(request):
    schools = KGardens.objects.order_by('name')
    context = {
        'schools':schools
    }
    return render(request, 'CRM/schools_table.html', context)


def classes_table(request):
    classes = Groups.objects.order_by('k_garden')
    context = {
        'classes':classes
    }
    return render(request, 'CRM/classes_table.html', context)


def classes_per_school(request, k_garden_id):
    school = KGardens.objects.get(id = k_garden_id)
    classes = Groups.objects.filter(k_garden_id = k_garden_id)
    context = {
        'classes': classes,
        'school': school,
    }
    return render(request, 'CRM/classes.html', context)

def children(request):
    children = Kids.objects.all()
    return render(request, 'CRM/children.html', {'children': children})

def gallery(request):
    pictures = KidPhotos.objects.order_by('updated_at')
    return render(request, 'CRM/gallery.html', {'pictures': pictures})


def gallery_kid(request, kid_id):
    kid_pics = KidPhotos.objects.filter(kid_id = kid_id)
    kid = Kids.objects.get(id = kid_id)
    return render(request, 'CRM/gallery_kid.html', {'kid_pics': kid_pics, 'kid':kid})


def gallery_class(request, group_id):
    kids = Kids.objects.filter(group_id=group_id)
    # class_name = Groups.objects.get(id = 361)
    # pics = KidPhotos.objects.all()
    return render(request, 'CRM/gallery_class.html', {'kids': kids})#, {'class': class_name, 'pics': pics})

def gallery_schools(request, k_garden_id):
    groups = Groups.objects.filter(k_garden = k_garden_id)
    school = KGardens.objects.get(id = k_garden_id)
    # kids = Kids.objects.filter(group_id = group.id)
    context = {
        'groups': groups,
        'school': school,
    }
    return render(request, 'CRM/gallery_schools.html', context)

def children_per_class(request, group_id):
    group = Groups.objects.get(id = group_id)
    children = Kids.objects.filter(group_id = group_id)
    context = {
        'group': group,
        'children': children,
    }
    return render(request, 'CRM/children.html', context)


def reports(request):
    # children = Child.objects.order_by('last_name')
    return render(request, 'CRM/reports.html')#, {'children': children})


def staff(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/staff.html')#, {'staff': staff})


def attendances(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/attendances.html')#, {'staff': staff})


def contacts(request):
    contacts = Contacts.objects.all()[:30]
    context = {
        'contacts': contacts,
    }
    return render(request, 'CRM/contacts.html', context)

def child_profile(request, kid_id):
    kid = Kids.objects.get(id = kid_id)
    contacts = Contacts.objects.filter(kid=kid_id)
    context = {
        'kid': kid,
        'contacts': contacts,
    }
    return render(request,'CRM/child_profile.html', context)

def staff_table(request):
    return render(request, 'CRM/staff_table.html')

def child_profile_health(request, kid_id):
    kid = Kids.objects.get(id = kid_id)
    context = {
        'kid': kid
    }
    return render(request, 'CRM/child_profile_health.html', context)


def child_profile_reports(request, kid_id):
    kid = Kids.objects.get(id = kid_id)
    return render(request, 'CRM/child_profile_reports.html', {'kid': kid})

