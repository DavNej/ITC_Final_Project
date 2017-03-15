from django.shortcuts import render, redirect
from django.template import loader
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
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

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def schools_table(request):
    schools = KGardens.objects.order_by('name')
    context = {
        'schools':schools
    }
    return render(request, 'CRM/schools_table.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists(), login_url='/')
def classes_table(request):
    classes = Groups.objects.order_by('k_garden')
    context = {
        'classes':classes
    }
    return render(request, 'CRM/classes_table.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def classes_per_school(request, k_garden_id):
    school = KGardens.objects.get(id = k_garden_id)
    classes = Groups.objects.filter(k_garden_id = k_garden_id)
    context = {
        'classes': classes,
        'school': school,
    }
    return render(request, 'CRM/classes.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists(), login_url='/')
def children(request):
    # next = request.GET.get('next')
    children = Kids.objects.all()
    # if next:
        # return redirect(next)
    return render(request, 'CRM/children.html', {'children': children})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def gallery(request):
    pictures = KidPhotos.objects.order_by('updated_at')
    return render(request, 'CRM/gallery.html', {'pictures': pictures})

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Parent').exists(), login_url='/')
def gallery_per_kid(request):
    kid_pics = KidPhotos.objects.filter(kid_id = 685)
    kid = Kids.objects.get(id = 685)
    return render(request, 'CRM/kid_gallery.html', {'kid_pics': kid_pics, 'kid':kid})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def gallery_per_class(request):
    class_name = Groups.objects.get(id = 361)
    pics = KidPhotos.objects.all()
    return render(request, 'CRM/class_gallery.html', {'class': class_name, 'pics': pics})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def children_per_class(request, group_id):
    group = Groups.objects.get(id = group_id)
    children = Kids.objects.filter(group_id = group_id)
    context = {
        'group': group,
        'children': children,
    }
    return render(request, 'CRM/children.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def schools(request):
    schools = KGardens.objects.order_by('name')
    example = KGardens.objects.get(id=201)
    context = {
        'schools':schools,
        'example':example,
    }
    return render(request, 'CRM/schools.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def reports(request):
    # children = Child.objects.order_by('last_name')
    return render(request, 'CRM/reports.html')#, {'children': children})


def staff(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/staff.html')#, {'staff': staff})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def attendances(request):
    # staff = Staff.objects.order_by('first_name')
    return render(request, 'CRM/attendances.html')#, {'staff': staff})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def contacts(request):
    # staff = Staff.objects.order_by('first_name')
    # school = KGardens.objects.get(id=k_garden_id)
    # group = Groups.objects.get(id=group_id)
    # children = Kids.objects.filter(group_id=group_id)
    contacts = Contacts.objects.all()[:30]
    
   #group = Groups.objects.get(id=group_id)
    #children = Kids.objects.filter(group_id=group_id)
    #contacts = Contacts.objects.filter(kid_id=kid_id)
    context = {
    #     'school': school.name,
        'contacts': contacts,
        
    #     'children': children,
    #
    }
    return render(request, 'CRM/contacts.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Connectoo').exists(), login_url='/')
def child_profile(request, kid_id):
    kid = Kids.objects.get(id = kid_id)
    return render(request,'CRM/child_profile.html', {'kid': kid})


def staff_table(request):
    return render(request, 'CRM/staff_table.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def child_profile_contact(request):
    return render(request, 'CRM/child_profile_contact.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def child_profile_medical(request):
    return render(request, 'CRM/child_profile_medical.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Teacher').exists(), login_url='/')
def child_profile_reports(request):
    return render(request, 'CRM/child_profile_reports.html')

